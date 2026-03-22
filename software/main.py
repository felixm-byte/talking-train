from machine import Pin, I2C, SDCard, I2S
import ssd1306
import time
import os
#some code based on miketeachman/micropython-i2s-examples

audio_enabled = True #toggle audio for the whole program e.g for testing in wokwi which lacks audio support

#switch_button = Pin(34, Pin.IN) button not in use

#creating I2C controller for SSD1306 OLED display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

if audio_enabled: #configure audio pinout and settings if audio is in use
    SCK_PIN = 32
    WS_PIN = 25
    SD_PIN = 33
    I2S_ID = 0
    BUFFER_LENGTH_IN_BYTES = 5000
    WAV_SAMPLE_SIZE_IN_BITS = 32
    FORMAT = I2S.STEREO
    SAMPLE_RATE_IN_HZ = 16000

sd = SDCard(slot=2)  #ESP£2 pins used: sck=18, mosi=23, miso=19, cs=5
os.mount(sd, "/sd")

def play_audio(filepath):
    wav = open(filepath, 'rb') #rb used for reading binary file format
    _ = wav.seek(44) # advances to first data piece, after metadata/headers
    wav_samples = bytearray(10000)
    wav_samples_mv = memoryview(wav_samples)
    try:
        while True:
            num_read = wav.readinto(wav_samples_mv)
            # end of WAV file?
            if num_read == 0:
                # end-of-file, documentation uses this command to advance to first byte of Data section:
                #_ = wav.seek(44)#
                #i want to end the output, not jump back to the start
                break
            else:
                _ = audio_out.write(wav_samples_mv[:num_read])
    except Exception as e:
        print(f"Error occured while playing {filepath}")
        print(f"Error details: {e}")
    



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
    global audio_enabled
    line = get_line_data("felix")
    try:
        wav_file = f"/sd/{line_name}_starting.wav"
        play_audio(wav_file)
    except Exception:
        audio_enabled = False

    for stop in line[2]:
        #data is displayed by the oled.text(a,b,c, d) function 
        #a: text, b: x-coord (width is 128), c: y-coord (height is 64), d: colour option (int)
        oled.text(f"{line[0]} line", 0, 0, 1)#this model only has one colour, this i
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