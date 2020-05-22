#include "Func.h"

int N = sizeof(x)/4;
float* f = new float[N];
uint8_t pin = 14;
uint32_t dt = 0;
void setup() {
  Serial.begin(115200);
  Serial.println("N = "+String(N));
  pinMode(pin, OUTPUT);
}

void loop() {
  dt = micros();
  digitalWrite(pin,HIGH);
  fft(x,f,N);
  digitalWrite(pin,LOW);
  dt = micros()-dt;
  for (int k = 0;k < N;k++){
    Serial.println("f[k="+String(k)+"] = "+String(f[k],8));
  }
  Serial.println("Duration: = "+String(dt)+"µs");
  delay(10000);
}
