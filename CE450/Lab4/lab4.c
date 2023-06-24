#include <stdio.h>
#include <wiringPi.h>

#define BUZZER 0
#define LED 1

int main(void) {
  if (wiringPiSetup() == -1) {
    printf("setup wiringPi failed!\n");
    printf("please check your setup\n");
    return -1;
  }

  pinMode(BUZZER, OUTPUT);
  digitalWrite(BUZZER, HIGH);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);

  while (1) {
    printf("Buzzer on\n");
    digitalWrite(BUZZER, LOW);
    digitalWrite(LED, LOW);
    delay(1024);
    digitalWrite(LED, HIGH);
    digitalWrite(BUZZER, HIGH);
    printf("Buzzer off\n");
    delay(1024);
  }

  return 0;
}