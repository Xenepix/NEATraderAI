import os

import pandas as pd
import numpy as np
from finta import TA

from lib.data_manager import DataManager

# Get dataframe
dm = DataManager(symbol='MATICBUSD')
dm.get_historical_klines(start_stop_day=(1, 31), kline_interval = '1h')
df = dm.dataframe
print(df)


# PCA dataframe
ma_list = [5, 10, 20, 50, 100, 200]
for ma in ma_list:
    df[f'ma{ma}'] = TA.SMA(df, ma)

df_pca = df[['close', 'ma5', 'ma10', 'ma20', 'ma50', 'ma100', 'ma200']].copy()
print(df_pca)
