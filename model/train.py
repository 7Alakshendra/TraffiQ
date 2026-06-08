import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = os.path.dirname(__file__)
data_path = os.path.join(BASE_DIR, '..', 'data', 'raw', 'Banglore_traffic_Dataset.csv')

df = pd.read_csv(data_path)
print(df.shape)