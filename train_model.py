# step 1: import required libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib 
import matplotlib.pyplot as plt


# step 2: load dataset
df = pd.read_csv('train.csv')

# step 3: handle missing data
features = ['OverallQual', 'GrLivArea', 'GarageCars',  'TotalBsmtSF', 'SalePrice']
df = df[features]
df = df.dropna()


#step 4: split data into train and test sets
X = df.drop('SalePrice', axis = 1)
y = df['SalePrice']

#step 5: train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#step 6: Train random forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#step 7: Evaluate model performance
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

# Step 7.1: Get feature importances
importances = model.feature_importances_
feature_names = X.columns

# Step 7.2: Create a bar chart
plt.figure(figsize=(8, 5))
plt.barh(feature_names, importances, color='skyblue')
plt.xlabel("Importance Score")
plt.title("Feature Importance for House Price Prediction")
plt.tight_layout()
plt.savefig("static/feature_importance.png")  # Save to static folder for Flask
plt.close()


#step 8: Save the trained model
joblib.dump(model, 'house_price_model.pkl')


