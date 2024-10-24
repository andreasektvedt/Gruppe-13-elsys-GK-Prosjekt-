const int sensorPin = 4;
const int LEDpin = 17;
int sensorValue;
const int threshold = 1200;
void setup(){
Serial.begin(9600);
pinMode(sensorPin, INPUT);
pinMode(LEDpin, OUTPUT);
}
void loop(){
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



