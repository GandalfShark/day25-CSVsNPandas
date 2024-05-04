# NOTES ON PANDAS

# import csv
#
# with open('weather_data.csv') as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)
#

import pandas

data = pandas.read_csv('weather_data.csv')
# the data here is a data frame which is all the data in the table
# print(type(data))
# print(type(data['temp']))
# you can index the imported pandas processed data by column name <class 'pandas.core.frame.DataFrame'>
# the complete contents of the column is collectively called a series <class 'pandas.core.series.Series'>
data_dict = data.to_dict()
# use the to_dict() function to turn all the DataFrame into a dictionary
temps_list = data['temp'].to_list()
# call the to_list() function on the Series 'temp' within the imported DataFrame


def get_average (numbers):
    return sum(numbers) / len(numbers)


average_temp = get_average(temps_list)
print(average_temp)
# long way with defining function

mean_temp = data['temp'].mean()
# big shock they do the same thing, takeaway = use the pandas functions when using pandas

max_temp = data['temp'].max()
print(f" Mean temperature is: {mean_temp}\n Max temperature is: {max_temp}")

print(data.condition)
# you don't need to index the data using ['column name'] you can get it with data.collumn
print('--------------')
print('the day with the highest temperature is: ')
print(data[data.temp == max_temp])
# print(data[data.temp == data.temp.max()]) <-- solution from challenge, IMHO my version = more readable
# checking for max temp in the print statement instead of call ing the var that stores the max temp
print (' _ _ _ _ _ _ _ _ _')


def cel_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


monday_temp = int(data[data.day == 'Monday']['temp'][0])
# get the day monday, at column temp at index zero and convert it to an int
print(f'The temperature on Monday in Fahrenheit was: {cel_to_fahrenheit(monday_temp)}')
