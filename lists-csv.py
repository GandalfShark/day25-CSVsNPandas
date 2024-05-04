
weather_list = []
with open ('weather_data.csv', 'r') as w:
    for line_in_file in w:
        weather_list.append(line_in_file.strip('\n'))
print(weather_list)

# solution given from challenge:
with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)
