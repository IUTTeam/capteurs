#include <math.h>

int receivedMessage;

int analogSensorPin = A5; // for KY-013 - Analog temperature

const int READ_ANALOG_TEMP = 1;

const String START_MESSAGE = "Successfully initialised";

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  Serial.setTimeout(20);
  Serial.println(START_MESSAGE);
}

void loop() {
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    receivedMessage = Serial.parseInt();
    switch (receivedMessage) {
      case READ_ANALOG_TEMP:
        Serial.println(readAnalogTemperature());
        break;
      default:
        Serial.println("ERROR");
        break;
    }
  }
}

double readAnalogTemperature() {
  int analogValue = analogRead(analogSensorPin);
  double temp;
  double rt;
  double voltage = 5.0 * analogValue / 1023.0;
  rt = 10000 * voltage / (5 - voltage);
  temp = 1 / (((log(rt / 10000)) / 3950) + (1 / (273.15 + 25)));
  temp = temp - 273.15;
  return temp;
}
