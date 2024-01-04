#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

const int ledPin = 5;

void setup() {
  Serial.begin(115200); // Initialize the serial communication
  SerialBT.begin("VENTILATOR");
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    // Create an array to store the received data
    char receivedData[4];
    
    // Read 3 bytes into the array
    int bytesRead = SerialBT.readBytes(receivedData, sizeof(receivedData) - 1);

    // Null-terminate the string
    receivedData[bytesRead] = '\0';

    // Process the received data as a string
    if (bytesRead > 0) {

      int receivedNumber = atoi(receivedData);

      // Process the received number
      receivedNumber=abs(255-receivedNumber);
      Serial.println(receivedNumber);

      analogWrite(ledPin, receivedNumber);
    }
  }
}



