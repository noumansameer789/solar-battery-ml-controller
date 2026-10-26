# ML-based adaptive solar battery controller

> **Provenance and scope.** BS Electrical Engineering final-year project, September 2024–June 2025, completed by a team of three. This cleaned reconstruction contains a control policy, tests and an ESP32 skeleton. Original hardware photographs and firmware are linked below. The original reported forecasting results have not been rerun by this repository.

BS Electrical Engineering final-year system joining next-day irradiance forecasting, embedded control
and battery-safety constraints.

## Reported result from the original prototype

- cleaned 26,000+ NASA POWER rows to 22,943 valid hourly observations, removing
  `-999` placeholders and anomalies
- chronological 80/20 evaluation: XGBoost MAE 32.44 Wh/m², RMSE 54.33 Wh/m²,
  R² 0.97; Random Forest baseline R² 0.956
- 500 Wh/m² sunny/not-sunny decision: 96.4% accuracy, 0.92 precision, 0.91
  recall and 0.91 F1
- Raspberry Pi 4 + ESP32 prototype on a battery pack, with
  dual-current sensing, SoC/SoH estimation, sub-50°C cutoff and ThingSpeak

## Executable portfolio layer

The Python policy makes the thermal override explicit and unit tested. The ESP32
file is a safe skeleton, not deployable firmware: sensor calibration, BMS limits,
relay fail-state and hardware-in-the-loop tests must be completed before use.

```bash
python -m unittest discover -s tests -v
```


## Original project evidence

[Original firmware and hardware archive](https://github.com/noumansameer789/ML-Based-Adaptive-Solar-Energy-Management-System-for-Optimised-Battery-Health-and-Efficiency) retains the team prototype and photographs. The archived ESP32 implementation uses ThingSpeak; Firebase is not supported by the inspected firmware. A trained model artefact is not supplied. The control skeleton here must not be treated as the original firmware.

## Licence

Original material is available for portfolio evaluation under the [evaluation-only licence](LICENSE). Third-party data, libraries and original assessment materials retain their own terms.

## Battery specification verification

Project descriptions conflict on the parallel-cell count (3S3P versus 3S9P). The available photograph does not independently establish the claimed 23.4 Ah pack capacity. The exact topology and capacity are therefore not presented as verified specifications. Confirm the wiring, cell ratings and measured capacity before reusing those figures. No battery-life or capacity-test result is implied by this archive.
