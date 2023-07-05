#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <wiringPi.h>
#include <wiringShift.h>

#define SDI 5
#define RCLK 4
#define SRCLK 1

const int placePin[] = {12, 3, 2, 0};
unsigned char letters[] = {0x88, 0x83, 0xa7, 0xa1, 0x86, 0x8e, 0xc2,
                           0x8b, 0xcf, 0xe1, 0x8a, 0xc7, 0xd4, 0xab,
                           0xa3, 0x8c, 0x98, 0xaf, 0x92, 0x87, 0xe3,
                           0xd5, 0x81, 0xb6, 0x91, 0x92, 0xff};
const char str[] = "hiyoudidgoodjob";
int idx = -1;

void pickDigit(int digit) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(placePin[i], 0);
  }
  digitalWrite(placePin[digit], 1);
}

void hc595_shift(int8_t data) {
  int i;
  for (i = 0; i < 8; i++) {
    digitalWrite(SDI, 0x80 & (data << i));
    digitalWrite(SRCLK, 1);
    delayMicroseconds(1);
    digitalWrite(SRCLK, 0);
  }
  digitalWrite(RCLK, 1);
  delayMicroseconds(1);
  digitalWrite(RCLK, 0);
}

void clearDisplay() {
  int i;
  for (i = 0; i < 8; i++) {
    digitalWrite(SDI, 1);
    digitalWrite(SRCLK, 1);
    delayMicroseconds(1);
    digitalWrite(SRCLK, 0);
  }
  digitalWrite(RCLK, 1);
  delayMicroseconds(1);
  digitalWrite(RCLK, 0);
}

void loop() {
  while (1) {
    if (idx) {
      clearDisplay();
      pickDigit(0);
      hc595_shift(letters[idx - 1]);
    }
    clearDisplay();
    pickDigit(1);
    hc595_shift(letters[idx]);

    if (str[idx] == '\0') {
      break;
    }
  }
}

void timer(int timer1) {
  if (timer1 == SIGALRM) {
    printf("%c\n", str[++idx]);
    alarm(1);
  }
}

int main(void) {
  if (wiringPiSetup() == -1) {
    printf("setup wiringPi failed !");
    return -1;
  }
  pinMode(SDI, OUTPUT);
  pinMode(RCLK, OUTPUT);
  pinMode(SRCLK, OUTPUT);

  for (int i = 0; i < 4; i++) {
    pinMode(placePin[i], OUTPUT);
    digitalWrite(placePin[i], HIGH);
  }
  signal(SIGALRM, timer);
  alarm(1);
  loop();
  return 0;
}