#include <stdio.h>
#include <wiringPi.h>

#define MotorPin1 0
#define MotorPin2 2
#define MotorEnable 3
#define YellowLED 5
#define RedLED 4

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

  digitalWrite(MotorEnable, LOW);
  //digitalWrite(YellowLED, HIGH);
  //digitalWrite(RedLED, HIGH);
  delay(2000);

  while (1) {
    printf("Clockwise\n");
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, HIGH);
    digitalWrite(MotorPin2, LOW);
    digitalWrite(YellowLED, LOW);
    digitalWrite(RedLED, HIGH);
    delay(3000);

    printf("Stop\n");
    digitalWrite(YellowLED, HIGH);
    digitalWrite(RedLED, LOW);
    digitalWrite(MotorEnable, LOW);
    delay(5000);

    printf("Anti-clockwise\n");
    digitalWrite(MotorEnable, HIGH);
    digitalWrite(MotorPin1, LOW);
    digitalWrite(MotorPin2, HIGH);
    digitalWrite(RedLED, LOW);
    digitalWrite(YellowLED, HIGH);
    delay(3000);

    printf("Stop\n");
    digitalWrite(MotorEnable, LOW);
    digitalWrite(RedLED, HIGH);
    digitalWrite(YellowLED, LOW);
    delay(5000);
  }
  return 0;
}
