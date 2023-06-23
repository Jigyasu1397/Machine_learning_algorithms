import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging as logger

from Cat_2_num import *
from Dataset import *
from Missingval import *

df_train = dataset()
df = df_train.copy()

# Dropping User ID column
df.drop(['User_ID'],axis=1,inplace=True)

# Categorical data to Numerical data
df_cat = cat_2_num(df)

# Handling missing values
data_mean_fillna1 = missing_val(df_cat)
logger.debug("Harmless debug Message")
print("It is reading")