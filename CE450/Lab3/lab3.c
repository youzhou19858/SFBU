#include <stdio.h>
#include <wiringPi.h>

#define UNIT_WAITING_TIME 128

void turn_on(int channel) { digitalWrite(channel, LOW); }

void turn_off(int channel) { digitalWrite(channel, HIGH); }

void dot() {
  turn_on(4);
  delay(UNIT_WAITING_TIME);
  turn_off(4);
}

void dash() {
  turn_on(5);
  delay(UNIT_WAITING_TIME << 1);
  turn_off(5)
}

void setup() {
  int i;
  for (i = 0; i < 8; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
  }
}

int main() {
  if (wiringPiSetup() == -1) {
    printf("setup wiringPi failed!\n");
    printf("please check your setup\n");
    return -1;
  }

  setup();
  const char code[64] = "- . ... - .---- ..--- ...--";
  int i = 0;
  while (code[i] != '\0') {
    switch (code[i]) {
      case '.':
        dot();
        break;
      case '-':
        dash();
      default:
        delay(UNIT_WAITING_TIME << 2);
        break;
    }
    ++i;
  }
  return 0;
}
