#include <stdio.h>
#include <wiringPi.h>

#define BeepPin 0

void turn_on(int channel) { digitalWrite(channel, LOW); }

void turn_off(int channel) { digitalWrite(channel, HIGH); }

int main(void) {
  if (wiringPiSetup() == -1) {
    printf("setup wiringPi failed !");
    return 1;
  }

  void setup() {
    for (int i = 0; i < 8; i++) {
      pinMode(i, OUTPUT);
      digitalWrite(i, HIGH);
    }
  }

  while (1) {
    // beep on
    printf("Buzzer on\n");
    digitalWrite(BeepPin, LOW);
    for (int i = 1; i < 8; ++i) {
      turn_on(7);
    }
    delay(100);
    for (int i = 1; i < 8; ++i) {
      turn_off(7);
    }
    printf("Buzzer off\n");
    // beep off
    digitalWrite(BeepPin, HIGH);
    delay(100);
  }

  return 0;
}