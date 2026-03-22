# talking-train
A model train with announcements for train stops

## File structure
Hardware files in /hardware - the .model file is for Asset Forge, which I am using to create the 3D models

Code in /software - these scripts are in MicroPython and target the ESP32 microcontroller, expecting a 128x64 SSD1306 I2C OLED display and an [I2S audio output device](https://github.com/miketeachman/micropython-i2s-examples)

##Part examples
- PCM5102 Digital I²S Audio Decoder DAC PCB 
- SSD1306 128x64
- ESP32

## Features
- Loads stations and displays them in order on the OLED screen
- Audio playback (semi-finished)
- Line creation tool
