# talking-train
![poster describing features of the talking train, with a features list and 3D model resembling a London Underground train](https://github.com/felixm-byte/talking-train/blob/main/docs/images/poster.png?raw=true)

## File structure
- Please ignore /hardware/old-design, for reference only
- Manufacturing files in hardware/manufacturing-outputs/...
- Code in /software - these scripts are in MicroPython and target the ESP32 microcontroller, expecting a 128x64 SSD1306 I2C OLED display and an [I2S audio output device](https://github.com/miketeachman/micropython-i2s-examples)
## Part examples
- SSD1306 128x64 display: https://www.aliexpress.com/item/1005007551771400.html
- Check Bill of Materials file for all other parts, these have LSCS part numbers for ease of ordering
- 4x M2 screws with nuts, 1cm length

## Features
- Loads stations and displays them in order on the OLED screen
- Audio playback with hi-res audio
- Line creation tool
- Audio playback support

## Key files
- hardware/manufacturing-outputs/ contains the files (.stl, pick and place, gerber, BOM) needed to produce the finished product, with the 3D files for the case in manufacturing-outputs/3d/ and the PCB in manufacturing-outputs/pcb/ 
- Source files like the EasyEDA (.epro) file and the 3D model of the PCB (only really necessary for designing a new case) is in hardware/source-files
- Use [the onshape file](https://cad.onshape.com/documents/c1f604bc7dcb19d0034320b9/w/e582f7a5ec8be5c9c5e2ed68/e/27ea5781da26a9e15f82bfe8?renderMode=0&uiState=69e37fad07cea94ea421e9c8) onshape for the case 3D source, and access an interactive bom on [my website](https://felix.ink/ttrain1)
- software/ contains the line creation tool and the software for the ESP32 to run.


## Assembly
- Assemble the PCB outside of the case by soldering on the parts. Do not attach the display at this stage. 
- To protect from the unlikely event of soldering error, do not plug the usb-c port directly into an important device: plug into a wall outlet first and check if the power LED is active. If not, I recommend stopping using the device.
- Then, attach the screen to the header, ensuring to align the parts such that all pins are connected to the header, and the display rests above the PCB. With the PCB aligned with the header on the left, the bottom pin-hole is for 'GND' and this should be connected to the leftmost pin 'GND' of the display.
- The parts of the model clip together. Once you have all parts soldered onto the board and attached to the board, screw the PCB into the 4 holes on the board, with the nuts on the outside of the board. Then, use the mounting clips and holes to align the 2 parts of the 3D model, and lower the pin side into the hole.

The pieces used for mounting the top half of the model:
![render of top piece](docs/images/top_piece.png)

Fit into these holes on the bottom part of the model.
![render of bottom piece](docs/images/bottom_piece.png)
## Graphics
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/docs/images/schematic.png?raw=true)
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/docs/images/pcb_visual.png?raw=true)
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/docs/images/pcb_visual2.png?raw=true)
![visualisation of a PCB](https://github.com/felixm-byte/talking-train/blob/main/docs/images/pcb_visual3.png?raw=true)
## Reference materials
- https://macsbug.wordpress.com/2021/02/19/web-radio-of-m5stack-pcm5102a-i2s-dac/ for DAC schematic
- https://documentation.espressif.com/esp32-c3_datasheet_en.pdf for ESP32-C3 datasheet
- https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf, especially Figure 24, for amplifier datasheet and schematic