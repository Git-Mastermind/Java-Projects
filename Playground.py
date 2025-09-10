import pandas as pd


students_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eshan"],
    "Age": [14, 16, 15, 18, 13],
    "Grade": ["9th", "10th", "9th", "12th", "8th"]
})



def first_3_rows():
    return students_data.head(3)

# print(first_3_rows())

def name_column():
    return students_data['Name']

# print(name_column())

def older_than_15():
    older_students = students_data[students_data['Age'] > 15]
    return older_students

print(older_than_15())
    



    