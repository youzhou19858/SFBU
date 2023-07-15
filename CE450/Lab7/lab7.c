#include <stdio.h>
#include <wiringPi.h>

#define MotorPin1 0
#define MotorPin2 2
#define MotorEnable 3
#define YellowLED 4
#define RedLED 5

int main(void) {
  if (wiringPiSetup() ==
      -1) {  // when initialize wiring failed, print message to screen
    printf("setup wiringPi failed !");
    return 1;
  }

  pinMode(MotorPin1, OUTPUT);
  pinMode(MotorPin2, OUTPUT);
  pinMode(MotorEnable, OUTPUT);
  pinMode(YellowLED, OUTPUT);
  pinMode(RedLED, OUTPUT);
  while (1) {
    printf("Clockwise\n");
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, HIGH);
    digitalWrite(MotorPin2, LOW);
    delay(200);
    digitalWrite(YellowLED, LOW);
    delay(6000);

    printf("Stop\n");
    digitalWrite(MotorEnable, LOW);
    delay(200);
    digitalWrite(YellowLED, HIGH);
    delay(200);

    printf("Anti-clockwise\n");
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, LOW);
    digitalWrite(MotorPin2, HIGH);
    delay(200);
    digitalWrite(RedLED, LOW);
    delay(6000);

    printf("Stop\n");
    digitalWrite(MotorEnable, LOW);
    delay(200);
    digitalWrite(RedLED, HIGH);
    delay(200);
  }
  return 0;
}