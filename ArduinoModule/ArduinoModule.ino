#include <math.h>

#define analogSensorPin A5 // for KY-013 - Analog temperature

#define trigPin 2 // for HC-SR04 - Ultrasound module
#define echoPin 3 //


const int READ_ANALOG_TEMP = 1;
const int READ_DISTANCE = 2;

const String START_MESSAGE = "Successfully initialised";

void setup() {
  // define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // begin serial communications and parameters
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  Serial.setTimeout(20);
  Serial.println(START_MESSAGE);
}

void loop() {
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    int receivedMessage = Serial.parseInt();
    switch (receivedMessage) {
      case READ_ANALOG_TEMP:
        Serial.println(readAnalogTemperature());
        break;
      case READ_DISTANCE:
        Serial.println(readDistance());
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

double readDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  // Trigger the sensor by setting the trigPin high for 10 microseconds:
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Read the echoPin, pulseIn() returns the duration (length of the pulse) in microseconds:
  long duration = pulseIn(echoPin, HIGH);
  // Calculate the distance:
  double distance = duration*0.034/2.;
  return distance;
  
}
