import os

import pandas as pd
import numpy as np
from finta import TA

# Setup dataframe
file_name = 'MATICBUSD-1h-2022-12-10.csv'
df = pd.read_csv(f'./{file_name}', parse_dates=True)
df = df.iloc[:, :6]
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

# PCA dataframe
ma_list = [5, 10, 20, 50, 100, 200]
for ma in ma_list:
    df[f'ma{ma}'] = TA.SMA(df, ma)

df_pca = df[['close', 'ma5', 'ma10', 'ma20', 'ma50', 'ma100', 'ma200']].copy()
print(df_pca)
