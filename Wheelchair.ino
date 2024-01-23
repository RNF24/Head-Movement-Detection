int RPWM1 = 5;  
int LPWM1 = 6; 
int R_EN1 = 7;
int L_EN1 = 4;
int RPWM2 = 10;  
int LPWM2 = 11; 
int R_EN2 = 9;
int L_EN2 = 8;

#include <avr/wdt.h>

char i = ‘1’;

void setup() {
  Serial.begin(9600);
  pinMode(RPWM1,OUTPUT);
  pinMode(LPWM1,OUTPUT);
  pinMode(R_EN1,OUTPUT);
  pinMode(L_EN1,OUTPUT);
  pinMode(RPWM2,OUTPUT);
  pinMode(LPWM2,OUTPUT);
  pinMode(R_EN2,OUTPUT);
  pinMode(L_EN2,OUTPUT);

  digitalWrite(R_EN1, HIGH);
  digitalWrite(L_EN1, HIGH);
  digitalWrite(R_EN2, HIGH);
  digitalWrite(L_EN2, HIGH);
  Serial.setTimeout(1);

  wdt_disable();  
  delay(1000); 
  wdt_enable(WDTO_2S);
}

void cepat(){
  analogWrite(LPWM1,0);
  analogWrite(RPWM1,60);
  analogWrite(LPWM2,0);
  analogWrite(RPWM2,60);
}

void maju(){
  analogWrite(LPWM1,0);
  analogWrite(RPWM1,40);
  analogWrite(LPWM2,0);
  analogWrite(RPWM2,40);
}

void berhenti(){
  analogWrite(LPWM1,0);
  analogWrite(RPWM1,0);
  analogWrite(LPWM2,0);
  analogWrite(RPWM2,0);
}

void kiri(){
  analogWrite(LPWM1,0);
  analogWrite(RPWM1,40);
  analogWrite(LPWM2,0);
  analogWrite(RPWM2,0);
}

void kanan(){
  analogWrite(LPWM1,0);
  analogWrite(RPWM1,0);
  analogWrite(LPWM2,0);
  analogWrite(RPWM2,40);
}

void loop() {
  if (Serial.available() > 0){
    char i = Serial.read();

    switch (i) {
      case '0':
        cepat();
        Serial.println("Mempercepat");
        break;

      case '1':
        berhenti();
        Serial.println("Berhenti");
        break;

      case '2':
        maju();
        Serial.println("Maju");
        break;

      case '3':
        kanan();
        Serial.println("Kanan");
        break;

      case '4':
        kiri();
        Serial.println("Kiri");
        break;
        
      default:
        break; 
    } 
   Serial.println(i);
  wdt_reset();
  }
}
