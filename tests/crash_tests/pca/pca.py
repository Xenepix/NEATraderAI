import os

import pandas as pd
import numpy as np
from finta import TA

from lib.data_manager import DataManager

# Get dataframe
dm = DataManager(symbol='MATICBUSD')
dm.get_historical_klines(start_stop_day=(1, 31), kline_interval = '1h')
df = dm.dataframe


# PCA dataframe
ma_list = [5, 10, 20, 50, 100, 200]
for ma in ma_list:
    df[f'ma{ma}'] = TA.SMA(df, ma)

df_pca = df[['close', 'ma5', 'ma10', 'ma20', 'ma50', 'ma100', 'ma200']].copy()
df_pca = df_pca.dropna()
df_pca = df_pca[['ma5', 'ma10', 'ma20', 'ma50', 'ma100', 'ma200']].apply(lambda x: x / df_pca['close'])
print(df_pca)

# PCA
from sklearn.decomposition import PCA
pca = PCA()
pca.fit(df_pca)

somme_proba = 0
for col in range(len(df_pca.columns)):
    somme_proba += pca.explained_variance_ratio_[col]
    print(f'PC{col} : {pca.explained_variance_ratio_[col]} - {100*somme_proba:0.2f} %')
    