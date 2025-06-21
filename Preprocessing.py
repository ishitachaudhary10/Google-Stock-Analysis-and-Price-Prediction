# Import necessary libraries and set up the environment
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')  # Ensure non-GUI backend
import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns

# For machine learning tasks
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Configure plot aesthetics
sns.set(style="whitegrid")

# Display basic configuration
print('Environment is set up.')

import kagglehub
import os
import pandas as pd

# Step 1: Download the dataset using kagglehub
path = kagglehub.dataset_download("adilshamim8/google-stocks-historical-data")
print("Dataset folder path:", path)

# Step 2: List all files in the dataset directory
files = os.listdir(path)
print("Files in dataset folder:", files)

# Step 3: Pick the correct file name (manually choose or from the list above)
# Let's assume the file is named "GOOGL.csv" — replace it with actual name shown
file_name = files[0]  # automatically picks the first file if you're unsure
file_path = os.path.join(path, file_name)

# Step 4: Load the file into a pandas DataFrame
df = pd.read_csv(file_path)

# Step 5: Display the first few rows
print("Dataset loaded. First few rows:")
df.head()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check for any missing or null values after conversion
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# If Date conversion resulted in NaT, it's important to note and possibly remove or impute these values
df = df.dropna(subset=['Date'])

# Reset index after dropping rows, if necessary
df.reset_index(drop=True, inplace=True)

# Show info to verify data types
print('\nData types after preprocessing:')
print(df.dtypes)
