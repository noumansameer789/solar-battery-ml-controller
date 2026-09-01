"""Safety-bounded charge scheduling policy for a solar battery prototype."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Telemetry:
    state_of_charge: float
    state_of_health: float
    temperature_c: float
    forecast_wh_m2: float


@dataclass(frozen=True)
class Decision:
    charge_fraction: float
    relay_enabled: bool
    reason: str


def decide(data: Telemetry, irradiance_threshold: float = 500.0,
           thermal_cutoff_c: float = 50.0) -> Decision:
    for value in (data.state_of_charge, data.state_of_health):
        if not 0.0 <= value <= 1.0:
            raise ValueError("SoC and SoH must be fractions between zero and one")
    if data.temperature_c >= thermal_cutoff_c:
        return Decision(0.0, False, "thermal_cutoff")
    if data.state_of_health < 0.7:
        return Decision(0.2, True, "battery_health_protection")
    if data.forecast_wh_m2 >= irradiance_threshold and data.state_of_charge < 0.8:
        return Decision(0.8, True, "sunny_forecast")
    if data.state_of_charge < 0.4:
        return Decision(0.4, True, "low_state_of_charge")
    return Decision(0.0, False, "hold")
