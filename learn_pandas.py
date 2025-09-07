import pandas as pd

def check_version():
    print(pd.__version__)

# check_version()

def create_dataframe():
    dataset = {
        'cars' : ['Tesla', 'Rivian', 'Lucid'],
        'passings' : [9,4,1]
    }

    my_dataset = pd.DataFrame(dataset)
    print(my_dataset)

# create_dataframe()

def create_series():
    nums = [1,5,8]
    series = pd.Series(nums, index=['num1', 'num2', 'num3'])
    print(series['num1'])

# create_series()

def dictionary_series():
    calories = {'day1':400, 'day2':390, 'day3':460}
    calorie_series = pd.Series(calories)
    print(calorie_series)

# dictionary_series()

def calories_dataframe():
    calories = {
        'calories':[400,390,460],
        'duration':[38,36,50]
    }
    calories_dataframe = pd.DataFrame(calories, index=['Day 1', 'Day 2', 'Day 3'])
    print(calories_dataframe)

# calories_dataframe()

def csv_dataframe():
    dataframe = pd.read_csv('data.csv')
    print(dataframe)

# csv_dataframe()

def csv_data():
    csv_data = pd.read_csv('data.csv')
    print(csv_data.to_string())

csv_data()



