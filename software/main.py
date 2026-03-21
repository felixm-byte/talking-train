from machine import Pin, I2C
import ssd1306
import time
import os
# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
switch_button = Pin(34, Pin.IN)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



def get_line_data(line_name):
    try: 
        file = open(f"{line_name}.txt", 'r')
    except Exception:
        file = open(f"jubilee_line.txt", 'r')
    txt = file.read()
    data = txt.split("\n")
    data[2] = data[2].split(",")
    return data



def display_line(line_name):
    line = get_line_data("felix")
    for stop in line[2]:
        oled.text(f"{line[0]} line", 0, 0, 1)#this model only has one colour
        oled.text(f"To: {line[1]}", 0, 15,1)
        oled.text(f"Calling at:", 0, 30,1)     
        oled.text(f"{stop}", 0, 45, 1)   
        oled.show()
        if switch_button.value() == 0:
            break
        time.sleep(5)
        oled.fill(0)

while True:
    print(switch_button.value())
    time.sleep(0.1)
#oled.fill(0)
#oled.text("Display complete.", 0,0,1)
#oled.text("Turn off and on to go again.", 0,25,1)
#oled.show()