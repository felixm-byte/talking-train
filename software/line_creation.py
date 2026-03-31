# this is in python and not intended to be ran on the microcontroller

def create_line_file(line_name, display_name, stations, audio_before, audio_after):
    line = open(f"{line_name}.lnfile", "w")
    text = f"{display_name} \n{stations[-1]} \n"
    for station in stations:
        text += f"{station} "
    text += "\n"
    for audio in audio_before:
        text += f"{audio} "
    text += "\n"
    for audio in audio_after:
        text += f"{audio} "
    line.write(text)

if 'y' in input("Create a new line? y/n").lower():
    print("If you make any mistakes you can restart the program.")
    line_name = input("Line name (include 'line' if necessary): ")
    file_name = input("File name for the line, in snake_case (no spaces!!): ")
    stations = []
    print("Enter the stations, from start to end, including the terminus.")
    print("Enter 's' to stop inputting stations")
    while True:
        station = input("Station name: ")
        if station.lower() != "s":
            stations.append(station)
        else:
            break
    audio_before = []
    while True:
        audio = input("Name of audio file to play BEFORE station name announcement, enter s to stop, enter *x where x is pause in seconds to pause: ")
        if audio.lower() != "s":
            audio_before.append(audio)
        else:
            break
    audio_after = []
    while True:
        audio = input("Name of audio file to play AFTER station name announcement, enter s to stop, enter *x where x is pause in seconds to pause: ")
        if audio.lower() != "s":
            audio_before.append(audio)
        else:
            break
    create_line_file(file_name, line_name, stations, audio_before, audio_after)