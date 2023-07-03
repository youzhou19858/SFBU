#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <wiringPi.h>
#include <wiringShift.h>

#define SDI 5
#define RCLK 4
#define SRCLK 1

const int placePin[] = {12, 3, 2, 0};
unsigned char number[] = {0xc0, 0xf9, 0xa4, 0xb0, 0x99,
                          0x92, 0x82, 0xf8, 0x80, 0x90};
unsigned char letters[] = {0x77, 0x1F, 0x4E, 0x3D, 0x4F, 0x47, 0x5E, 0x37, 0x06,
                           0x3C, 0x57, 0x0E, 0x55, 0x15, 0x1D, 0x67, 0x73, 0x05,
                           0x5B, 0x0F, 0x3E, 0x1C, 0x5C, 0x13, 0x3B, 0x6D};

int counter = 0;
int idxOfLetter = 0;

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
    clearDisplay();
    pickDigit(0);
    hc595_shift(number[(counter % 25 + 1) % 10]);

    clearDisplay();
    pickDigit(1);
    hc595_shift(number[(counter % 25 + 1) % 100 / 10]);

    clearDisplay();
    pickDigit(2);
    hc595_shift(letters[idxOfLetter % 26]);

    // clearDisplay();
    // pickDigit(3);
    // hc595_shift(number[counter % 10000 / 1000]);
  }
}

void timer(int timer1) {
  if (timer1 == SIGALRM) {
    counter++;
    idxOfLetter++;
    alarm(1);
    printf("%d\n", counter);
  }
}

int main(void) {
  if (wiringPiSetup() == -1) {
    printf("setup wiringPi failed !");
    return;
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
}