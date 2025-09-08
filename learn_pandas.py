import pandas as pd
import matplotlib.pyplot as mat

def check_version():
    print(pd.__version__)

# check_version()

def max_rows():
    print(pd.options.display.max_rows)

# max_rows()

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
    print(csv_data.to_html())


# csv_data()

def dictionary_dataframe():
    
    data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
    },
    "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
    },
    "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
    },
    "Calories":{
        "0":409,
        "1":479,
        "2":340,
        "3":282,
        "4":406,
        "5":300
    }
    }
    df = pd.DataFrame(data)
    print(df)

# dictionary_dataframe()

def drop_empty_cells():
    dataframe = pd.read_csv('data.csv')
    dataframe.dropna(inplace=True)
    print(dataframe)


# drop_empty_cells()

def fill_empty_cells():
    dataframe = pd.read_csv('data.csv')
    avg_calorie = dataframe['Calories'].mean()
    dataframe.fillna(avg_calorie, inplace=True)
    print(dataframe)

# fill_empty_cells()

def convert_format_of_date():
    dataframe = pd.read_csv('data.csv')
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='mixed')
    print(dataframe.to_string())

# convert_format_of_date()

def fix_wrong_data():
    data = pd.read_csv('data.csv')
    data.loc[7, 'Duration'] = 45
    print(data.to_string())

# fix_wrong_data()

def fix_all_wrong_data():
    data = pd.read_csv('data.csv')
    for i in data.index:
        if data.loc[i, 'Duration'] > 120:
            data.loc[i, 'Duration'] = 120
    
    print(data.to_string())

# fix_all_wrong_data()

def find_duplicates():
    data = pd.read_csv('data.csv')
    print(data.duplicated())

# find_duplicates()

def delete_duplicates():
    data = pd.read_csv('data.csv')
    data.drop_duplicates(inplace=True)
    print(data.to_string())

# delete_duplicates()

def correlation():
    data = pd.read_csv('data.csv')
    return data.corr()
    

# print(correlation())

def data_graphing():
    data = pd.read_csv('data.csv')
    data.plot()
    mat.show()

data_graphing()





