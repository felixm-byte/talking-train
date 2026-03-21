def create_line_file(line_name, display_name, stations):
    line = open(f"{line_name}.txt", "w")
    text = f"{display_name} \n{stations[-1]} \n"
    for station in stations:
        text += f"{station} "
    line.write(text)

create_line_file("felix", "Felix", ["London", "HK", "Shenzhen"])
