
/*
   tx-rx-01.ino -  

   Envia la cantidad de asteriscos
   especificada por el caracter ascii recibido
   
   Ej. recibe '6' enva '******' 
   
   Copyright 2016 - Diego Codevilla - <dcodevilla@pioix.edu.ar>
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  
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


