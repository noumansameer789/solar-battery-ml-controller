// Portfolio-safe control skeleton. Hardware limits must be calibrated before use.
const int RELAY_PIN = 5;
const float THERMAL_CUTOFF_C = 50.0;

float readTemperatureC() {
  // Replace with the calibrated sensor driver used by the physical prototype.
  return 25.0;
}

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
  Serial.begin(115200);
}

void loop() {
  const float temperature = readTemperatureC();
  if (temperature >= THERMAL_CUTOFF_C) {
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("THERMAL_CUTOFF");
  }
  delay(1000);
}
