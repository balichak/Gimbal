#include <Servo.h>

Servo panServo;
Servo tiltServo;

int panPin = 9;
int tiltPin = 10;

void setup() {
  panServo.attach(panPin);
  tiltServo.attach(tiltPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int panAngle = Serial.parseInt();
    int tiltAngle = Serial.parseInt();
    panServo.write(panAngle);
    tiltServo.write(tiltAngle);
  }
}

