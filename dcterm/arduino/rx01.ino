/*
 enva por puerto serie el valor de conversion 
 de un ADC - pata AI 0
 */

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
}

void loop() {
  // send the value of analog input 0:
  Serial.println(analogRead(0));

  delay(2000);
}