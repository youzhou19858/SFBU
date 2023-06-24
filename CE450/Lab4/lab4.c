/**********************************************************************
 * Filename    : beep.c
 * Description : make a buzzer beep.
 * Author      : Robot
 * E-mail      : support@sunfounder.com
 * website     : www.sunfounder.com
 * Update      : Cavon    2016/07/01
 **********************************************************************/
#include <stdio.h>
#include <wiringPi.h>

#define BeepPin 0

int main(void) {
  if (wiringPiSetup() ==
      -1) {  // when initialize wiring failed, print messageto screen
    printf("setup wiringPi failed !");
    return 1;
  }

  pinMode(BeepPin, OUTPUT);  // set GPIO0 output

  while (1) {
    // beep on
    printf("Buzzer on\n");
    digitalWrite(BeepPin, LOW);
    delay(100);
    printf("Buzzer off\n");
    // beep off
    digitalWrite(BeepPin, HIGH);
    delay(100);
  }

  return 0;
}