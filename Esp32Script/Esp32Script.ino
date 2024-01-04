#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

const int ledPin = 5;

void setup() {
  Serial.begin(115200); // Initialize the serial communication
  SerialBT.begin("Esp32-BT");
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    char c = SerialBT.read();
    int command = int(c);

    Serial.println("Received command: " + String(command)); // Print the received command to the serial monitor
    
    analogWrite(ledPin, command);
  }
}
