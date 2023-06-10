#include <wiringPi.h>
#include <stdio.h>

void turn_on(int channel){
  digitalWrite(channel,LOW);
}

void turn_off(int channel){
  digitalWrite(channel,HIGH);
}

void setup(){
  int i;
  for(i=0;i<8;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,HIGH);
  }
}

int main(){
  int i;
  if(wiringPiSetup()==-1){
    printf("setup wiringPi failed!\n");
    printf("please check your setup\n");
    return -1;
  }

  setup();
  while(1){
    for(i=0;i<8;i++){
      turn_on(i);
      delay(512);
      turn_off(i);
    } 
    for(i=7;i>=0;i--){
      turn_on(i);
      delay(512);
      turn_off(i);
    }
  }
  return 0;
}
