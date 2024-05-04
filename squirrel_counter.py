"""
day 25 challenge working with squirrel census data
import the data from squirrel census
count the squirrels by Primary Fur Color and output the total
use pandas to process the data and make a new DataFrame with the count
export that data frame to a CSV
"""

import pandas as pd

black_squirrels = 0
gray_squirrels = 0
cinnamon_squirrels = 0

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = data['Primary Fur Color']

for color in colors:
    if color == 'Gray':
        gray_squirrels += 1
    if color == 'Cinnamon':
        cinnamon_squirrels += 1
    if color == 'Black':
        black_squirrels += 1
    else:
        pass
# could have used len function instead

color_count_dict = {
    'colors': ['Gray', 'Cinnamon', 'Black'],
    'squirrel count': [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

squirrel_data = pd.DataFrame(color_count_dict)
print(squirrel_data)

squirrel_data.to_csv('squirrel_count.csv')
print('\ncount data written to: squirrel_count.csv')