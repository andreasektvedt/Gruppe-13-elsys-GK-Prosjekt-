const int potPin = 36;  // Bruk en ADC1-pin (for eksempel GPIO 36)
const float lowerThreshold = 0.8;  // Nedre spenningsgrense
const float upperThreshold = 2.5;  // Øvre spenningsgrense

void setup() {
  Serial.begin(115200);  // Start seriell kommunikasjon
}

void loop() {
  // Les den analoge verdien fra potensiometeret (ADC1)
  int analogValue = analogRead(potPin);

  // Konverter den analoge verdien til spenning (0 - 3.3V)
  float voltage = analogValue * (3.3 / 4095.0);

  // Sjekk om spenningen er mellom 0.8V og 2.5V
  if (voltage >= lowerThreshold && voltage <= upperThreshold) {
    Serial.println("Døren skal lukkes");
  }
  
  // For debugging kan vi også skrive spenningen til seriell monitor
  Serial.print("Analog verdi: ");
  Serial.print(analogValue);
  Serial.print(" - Spenning: ");
  Serial.println(voltage, 3);  // Vis spenning med 3 desimaler

  delay(500);  // Vent litt før neste måling
}
