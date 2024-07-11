# Import Modules
import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv('C:/VS CODE/ML/Feature Scaling/SampleFile.csv')
print(df.head())

# Robust Scaling
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data,
                         columns=df.columns)

print('\nScaled data:')
print(scaled_df.head())