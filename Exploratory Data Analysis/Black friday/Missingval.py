import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def missing_val(df_cat):
    data_copy = df_cat.copy()
    data_mean_fillna = df_cat.copy()
    mean_data = data_copy.mean(axis=0,numeric_only=True,skipna=True)
    for features in data_copy.columns:
        # print(features)
        data_mean_fillna[features] = data_copy[features].fillna(value=mean_data[features]) 
    return data_mean_fillna