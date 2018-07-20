# Use sci mode
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# %%
# Read data
df = pd.read_csv('_sklearn/bento.csv')

# %%
# Map data from str to int
df['youbi'] = df['youbi'].map({'月': 0, '火': 1, '水': 2, '木': 3, '金': 4})
df['weather'] = df['weather'].map({'快晴': 0, '晴れ': 1, '薄曇': 2, '曇': 3, '雨': 4, '雪': 5, '雷電': 6})

# %%
# Choose reference(x) and destination(y)
x = df[['youbi', 'weather', 'temp']]
y = df[['num_sales']]

# %%
# Split data into train data and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# %%
# Train linear regression model
lr = LinearRegression()
lr.fit(x_train, y_train)

# %%
# Predict
y_pred = lr.predict(x_test)

# Use RMSE to evaluate model
err = np.sqrt(mean_squared_error(y_test, y_pred))
