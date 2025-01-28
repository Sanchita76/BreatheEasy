import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_future_aqi():
    # Load and prepare data
    data = pd.read_csv("data/aqi_history.csv")
    data['Days'] = np.arange(len(data))  # Create numeric days column
    
    X = data[['Days']]
    y = data['AQI']

    model = LinearRegression()
    model.fit(X, y)

    # Predict the next 7 days
    future_days = np.arange(len(data), len(data) + 7).reshape(-1, 1)
    predictions = model.predict(future_days)

    print("Predicted AQI for next 7 days:", predictions)
    return predictions

if __name__ == "__main__":
    predict_future_aqi()
