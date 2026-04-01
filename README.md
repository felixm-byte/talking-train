# talking-train
![poster describing features of the talking train, with a features list and 3D model resembling a London Underground train](https://github.com/felixm-byte/talking-train/blob/main/poster.png?raw=true)
## File structure
Hardware files in /hardware - the .model file is for Asset Forge, which I am using to create the 3D models

Code in /software - these scripts are in MicroPython and target the ESP32 microcontroller, expecting a 128x64 SSD1306 I2C OLED display and an [I2S audio output device](https://github.com/miketeachman/micropython-i2s-examples)

## Part examples
- PCM5102 Digital I²S Audio Decoder DAC PCB 
- SSD1306 128x64
- ESP32
- Check Bill of Materials file for all parts

## Features
- Loads stations and displays them in order on the OLED screen
- Audio playback with hi-res audio
- Line creation tool
- Audio playback support

## Key files
- hardware/working-model.stl is the final 3D model - you can upload this straight to JLC3DP and print out
- hardware/BOM.xlsx is the bill of materials
- hardware/Gerber_V1 is the Gerber file for PCB production
- software/ contains the line creation tool and the software for the ESP32 to run.

## Graphics
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/schematic.png?raw=true)
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/pcb_visual.png?raw=true)
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/pcb_visual2.png?raw=true)

## Reference materials
- https://macsbug.wordpress.com/2021/02/19/web-radio-of-m5stack-pcm5102a-i2s-dac/ for DAC schematic
- https://documentation.espressif.com/esp32-c3_datasheet_en.pdf for ESP32-C3 datasheet
- https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf, especially Figure 24, for amplifier datasheet and schematic