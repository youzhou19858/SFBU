#include <stdio.h>
#include <wiringPi.h>

#define BUZZER 17
#define LED 18

int main(void) {
  pinMode(BUZZER, OUTPUT);
  digitalWrite(BUZZER, HIGH);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);

  while (1) {
    printf("Buzzer on\n");
    digitalWrite(BUZZER, LOW);
    digitalWrite(LED, LOW);
    delay(256);
    digitalWrite(LED, HIGH);
    digitalWrite(BUZZER, HIGH);
    printf("Buzzer off\n");
    delay(128);
  }

  return 0;
}