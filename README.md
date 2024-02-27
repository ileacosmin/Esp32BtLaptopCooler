# Laptop Cooler Control App

This project is a Python application for controlling a laptop cooler via Bluetooth. It provides a graphical user interface (GUI) for discovering nearby Bluetooth devices and sending commands to control the cooler's fan speed. The app is designed to adjust the fan speed of the laptop cooler connected to a pin on the board using the GUI.

## Features

- Discover nearby Bluetooth devices
- Display a list of discovered devices
- Control the fan speed of the laptop cooler
- Use a slider to adjust the fan speed

## Usage

1. Run the Python script `Main.py`.
2. Click on the "Discover Devices" button to find nearby Bluetooth devices.
3. Select the desired device from the list.
4. Use the "Turn ON FAN" and "Turn OFF FAN" buttons to control the laptop cooler.
5. Adjust the fan speed using the slider.

## Uploading Script to the Board

Before using the Laptop Cooler Control App, make sure to upload the provided script (`Esp32Script.ino`) to your ESP32 board. This script enables the ESP32 to receive commands from the Laptop Cooler Control App.

## Installation

1. Clone the repository:

   ```bash
   $ git clone https://github.com/pierpatrat/Esp32BtLaptopCooler.git
   $ cd Esp32BtLaptopCooler
2. Install the required libraries
  
    ```bash
    $ pip install bluetooth
    $ pip install customtkinter
