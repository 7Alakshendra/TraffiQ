import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split 

BASE_DIR = os.path.dirname(__file__)
data_path = os.path.join(BASE_DIR, '..', 'data', 'raw', 'Banglore_traffic_Dataset.csv')

df = pd.read_csv(data_path)
df["Date"]=pd.to_datetime(df["Date"])
df['DayofWeek'] = df['Date'].dt.dayofweek
df['Month'] = df['Date'].dt.month
print(df.info())

features = [
    'Area Name',
    'Traffic Volume',
    'Average Speed',
    'Travel Time Index',
    'Weather Conditions',
    'Roadwork and Construction Activity',
    'DayofWeek',
    'Month'
]

target = 'Congestion Level'

X = df[features]
y = df[target]

print(X.shape)
print(y.shape)
print(X.info())

cat_cols=["Area Name","Weather Conditions","Roadwork and Construction Activity"]

X=pd.get_dummies(X,columns=cat_cols,drop_first=True)

print(X.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape,X_test.shape)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)
print("Model Trained")

predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae=mean_absolute_error(y_test,predictions)
r2=r2_score(y_test,predictions)

print("MAE:", mae)
print("R²:", r2)

feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print(feature_importance.sort_values(ascending=False))