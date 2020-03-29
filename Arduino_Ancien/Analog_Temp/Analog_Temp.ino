#include <math.h>
 
int sensorPin = A5; // select the input pin for the potentiometer
 
double convertToTemperature(int analogValue) {
  double temp;
  double rt;
  double voltage = 5.0 * analogValue / 1023.0;
  rt = 10000 * voltage / (5 - voltage);
  temp = 1 / (((log(rt / 10000)) / 3950) + (1 / (273.15 + 25)));
  temp = temp - 273.15;
  return temp;
}
 
void setup() {
 Serial.begin(9600);
}
 
void loop() {
 int readVal= analogRead(sensorPin);
 double temp = convertToTemperature(readVal);
 
 Serial.println(temp);  // display tempature
 //Serial.println(readVal);  // display tempature
 
 delay(1000);
}
