# Entraîner une régression linéaire simple sur un dataset simple (par exemple houses.csv) et le sauvegarder
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('houses.csv')

X = df.drop(columns = ['price', 'orientation'])
y = df['price']

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print(y_pred)
print(model.score(X,y)) # ?
joblib.dump(model, 'linear_regression.joblib')