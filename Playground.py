import pandas as pd
import numpy as np
import matplotlib.pyplot as mat

data = pd.read_csv('sales.csv')
avg_burgers = np.mean(data['Burgers'])
print(f'Avg Burgers sold: {avg_burgers}')