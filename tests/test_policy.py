import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from solar_controller.policy import Telemetry, decide


class PolicyTest(unittest.TestCase):
    def test_thermal_cutoff_overrides_forecast(self):
        decision = decide(Telemetry(0.2, 0.9, 51.0, 900.0))
        self.assertFalse(decision.relay_enabled)
        self.assertEqual(decision.reason, "thermal_cutoff")

    def test_sunny_charge(self):
        self.assertEqual(decide(Telemetry(0.5, 0.9, 25, 600)).charge_fraction, 0.8)


if __name__ == "__main__":
    unittest.main()
