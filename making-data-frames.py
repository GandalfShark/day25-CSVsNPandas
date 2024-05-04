import pandas as pd

data_dict = {
    "students": ['John', 'Paul', 'George', 'Ringo'],
    "scores": [90, 80, 79, 100]
}

data = pd.DataFrame(data_dict)
data.to_csv('student_data.csv')