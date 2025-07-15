import pandas as pd

def ages_to_names():
    ages = pd.Series([12,13,14], index=['Eshan', 'Ali', 'Lily'])
    print(ages)

# ages_to_names()

def cars_model_dataset():
    cars_model = {
        'cars' : ['Tesla', 'Rivian', 'Range Rover'],
        'model' : ['Cybertruck', 'R1S', 'Land Rover']
    }
    cars_model_dataframe = pd.DataFrame(cars_model)
    print(cars_model_dataframe)

# cars_model_dataset()

def fruit_series():
    fruits = ['apples', 'strawberries', 'blueberries', 'cherries', 'grapes']
    series = pd.Series(fruits, index=['a', 'b', 'c', 'd', 'e'])
    print(series)

# fruit_series()

def dictionary_series():
    calories = {'day1':300, 'day2':400, 'day3':600}
    calorie_series = pd.Series(calories, index=['day1', 'day2', 'day3'])
    print(calorie_series)
    
# dictionary_series()

def pandas_dataframes():
    calorie_data = {
        'calories' : [500, 502, 600, 700, 420, 501],
        'duration' : [47, 46, 56, 63, 39, 43]
    }
    calorie_duration_dataframed = pd.DataFrame(calorie_data)
    print(calorie_duration_dataframed)

# pandas_dataframes()

def pandas_read_csv():
    df = pd.read_csv('data.csv')
    print(df)

pandas_read_csv()

# For printing max rows avalile:
#   print(pd.options.display.max_rows)

def pandas_clean_cells():
    df = pd.read_csv('data.csv')
    df.fillna(69, inplace=True)
    print(df.to_string())

pandas_clean_cells()