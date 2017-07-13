# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np # Mathematical tools
import matplotlib.pyplot as plt # Plotting/visualization tools
import pandas as pd # Data set management tool

raw_data = pd.read_csv('raw_data.csv')
features = raw_data.iloc[:, :-1].values
dependent_variable = raw_data.iloc[:, 4].values

# Fixing missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0)
imputer = imputer.fit(features[:, 0:2])
features[:, 0:2] = imputer.transform(features[:, 0:2])