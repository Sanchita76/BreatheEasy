import pandas as pd
import matplotlib.pyplot as plt

def plot_aqi_trend():
    # Load historical data
    data = pd.read_csv("data/aqi_history.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['AQI'], label="AQI Levels", color='blue')
    plt.xlabel("Date")
    plt.ylabel("Air Quality Index (AQI)")
    plt.title("Air Quality Trends Over Time")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_aqi_trend()