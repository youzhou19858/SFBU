#include <stdio.h>
#include <wiringPi.h>

#define BLINKING_TIME 256
#define UNIT_WAITING_TIME 1024

void turn_on(int channel) { digitalWrite(channel, LOW); }

void turn_off(int channel) { digitalWrite(channel, HIGH); }

void dot() {
  turn_on(3);
  delay(BLINKING_TIME);
  turn_off(3);
  delay(UNIT_WAITING_TIME);
}

void dash() {
  turn_on(2);
  delay(BLINKING_TIME);
  turn_off(2);
  delay(UNIT_WAITING_TIME << 1);
}

void interval() {
  turn_on(5);
  delay(BLINKING_TIME);
  turn_off(5);
  delay(UNIT_WAITING_TIME << 2);
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
  const char code[] = "- . ... - .---- ..--- ...--";
  int i = 0;
  while (code[i] != '\0') {
    if (code[i] == '.') {
      dot();
    } else if (code[i] == '-') {
      dash();
    } else {
      interval();
    }
    ++i;
  }
  return 0;
}
