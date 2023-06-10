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
  if(wiringPiSetup()==-1){
    printf("setup wiringPi failed!\n");
    printf("please check your setup\n");
    return -1;
  }

  setup();
  int l = 3;
  int r = 4;
  while(1){
    turn_on(l);
    turn_on(r);
    delay(512);
    turn_off(l);
    turn_off(r);
    --l; ++r;
    if(r==8){
      l = 7;
      r = 0;
    }
    if(r==3){
      l = 3;
      r = 4;
    }
  }
  return 0;
}
