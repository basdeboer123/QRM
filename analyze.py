import numpy as np
import pandas as pd

data = pd.read_csv('prepared_data.csv', sep='\t', index_col=0)
print(data.isna().sum())
