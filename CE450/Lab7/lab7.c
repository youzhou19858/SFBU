#include <stdio.h>
#include <wiringPi.h>

#define MotorPin1 0
#define MotorPin2 2
#define MotorEnable 3
#define YellowLED 4
#define RedLED 5

int main(void) {
  int i;
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
    delay(100);
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, HIGH);
    digitalWrite(MotorPin2, LOW);
    digitalWrite(YellowLED, LOW);
    delay(5000);

    printf("Stop\n");
    delay(100);
    digitalWrite(MotorEnable, LOW);
    digitalWrite(YellowLED, HIGH);
    delay(2000);

    printf("Anti-clockwise\n");
    delay(100);
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, LOW);
    digitalWrite(MotorPin2, HIGH);
    digitalWrite(RedLED, LOW);
    delay(5000);

    printf("Stop\n");
    delay(100);
    digitalWrite(MotorEnable, LOW);
    digitalWrite(RedLED, HIGH);
    delay(2000);
  }
  return 0;
}