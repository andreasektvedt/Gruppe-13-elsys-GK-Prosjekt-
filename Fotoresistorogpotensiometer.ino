const int sensorPin = 4;
const int LEDpin = 17;
int sensorValue;
const int threshold = 800;
const int potPin = 36;  // Bruk en ADC1-pin (for eksempel GPIO 36)
const float lowerThreshold = 0.8;  // Nedre spenningsgrense
const float upperThreshold = 2.5;  // Øvre spenningsgrense
void setup(){
Serial.begin(9600);
Serial.begin(115200);
pinMode(sensorPin, INPUT);
pinMode(LEDpin, OUTPUT);
}
void loop(){
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
sensorValue = analogRead(sensorPin);
Serial.print(sensorValue, DEC);
Serial.print(" \n");
if (sensorValue > threshold){
digitalWrite(LEDpin, LOW);
}
else {
digitalWrite(LEDpin, HIGH);
}
delay(1000);
}


