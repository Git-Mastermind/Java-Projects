import numpy as np
import pandas as pd

data = {
    'name':'Eshan',
    'age':13,
    'studend ID':1078890,
    'gender':'Male'
}
df = pd.DataFrame(data)
print(df.to_string())