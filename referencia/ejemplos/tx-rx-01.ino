/*
Envia la cantidad de asteriscos
especificada por el caracter ascii recibido
Ej. recibe '6' enva '******'
 */

void setup()
{
  // initialize the serial communication:
  Serial.begin(9600);
}

void loop() {
  unsigned char car;
  // check if data has been sent from the computer:
  if (Serial.available()) {
      car = Serial.read();
      
      for (int i = 0; i < car - 0x30; i++) {
          Serial.write("*");
      }
      Serial.write( "\n");
  }
}


