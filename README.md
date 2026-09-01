# ML-based adaptive solar battery controller

BEng final-year system joining next-day irradiance forecasting, embedded control
and battery-safety constraints.

## Reported result from the original prototype

- cleaned 26,000+ NASA POWER rows to 22,943 valid hourly observations, removing
  `-999` placeholders and anomalies
- chronological 80/20 evaluation: XGBoost MAE 32.44 Wh/m², RMSE 54.33 Wh/m²,
  R² 0.97; Random Forest baseline R² 0.956
- 500 Wh/m² sunny/not-sunny decision: 96.4% accuracy, 0.92 precision, 0.91
  recall and 0.91 F1
- Raspberry Pi 4 + ESP32 prototype on a 3S9P, 11.1 V, 23.4 Ah pack, with
  dual-current sensing, SoC/SoH estimation, sub-50°C cutoff and ThingSpeak

## Executable portfolio layer

The Python policy makes the thermal override explicit and unit tested. The ESP32
file is a safe skeleton, not deployable firmware: sensor calibration, BMS limits,
relay fail-state and hardware-in-the-loop tests must be completed before use.

```bash
python -m unittest discover -s tests -v
```
