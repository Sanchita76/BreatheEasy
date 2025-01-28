# 🏭 💨 BreatheEasy - Real-Time Air Quality Monitoring System 🌬️

**BreatheEasy** is a real-time air quality monitoring system that uses OpenWeatherMap's Air Pollution API to track and predict the Air Quality Index (AQI) of a given location. This project aims to raise awareness about air pollution and provide users with actionable recommendations to protect their health based on the AQI levels. 

## 🧾 Key Features ⛓️‍💥

- **Real-Time AQI Data**: Displays real-time AQI data based on your location.
- **Historical Data Visualization**: Visualizes historical AQI trends to observe air quality changes over time.
- **Predictive Analysis**: Uses machine learning to predict AQI trends for the next few days.
- **Health Recommendations**: Provides health recommendations based on current AQI levels.

## 👨‍💻 Technologies Used 🤖 

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Custom Styling)
- **API**: OpenWeatherMap Air Pollution API
- **Data Visualization**: Matplotlib
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Version Control**: GitHub

## 📁 File Structure 
BreatheEasy/<br>
│-- static/                   # Frontend assets (CSS, JS, images)<br>
│   ├── css/<br>
│   │   ├── style.css         # Custom CSS for styling <br>
│   ├── js/ <br>
│   │   ├── script.js         # Client-side interactivity<br>
│   ├── images/<br>
│   │   ├── air_quality_icon.png  # Icons or banners <br>
│-- templates/                # HTML templates for Flask<br>
│   ├── index.html            # Main webpage<br>
│-- data/                     # Store historical data (CSV, JSON)<br>
│   ├── aqi_history.csv       # Past AQI data<br>
│   ├── sample_data.json      # Sample API response data<br>
│-- src/<br>
│   ├── app.py                # Flask web application<br>
│   ├── fetch_aqi.py          # Script to fetch AQI data<br>
│   ├── visualize_aqi.py      # Data visualization logic<br>
│   ├── predict_aqi.py        # Machine learning model<br>
│-- README.md                 # Project documentation<br>
│-- requirements.txt          # Dependencies list<br>

## Usage 👍<br>
- **Real-time AQI Data:** The system fetches and displays the current AQI value for a predefined location (can be adjusted to user input or GPS).<br>
- **Historical Data Visualization:** The visualize_aqi.py script generates plots showing AQI trends over time.<br>
- **Predictive Analysis:** The predict_aqi.py script uses linear regression to predict AQI for the next 7 days.<br>
- **Health Recommendations:** Based on the AQI, the system provides recommendations such as "Safe", "Moderate", or "Unhealthy" and suggests precautions to take.<br>

## Setup Instructions<br> 🚀
1. **Clone the repository**:
   git clone https://github.com/Sanchita76/BreatheEasy.git <Enter><br>
   cd BreatheEasy <Enter><br>
2. **Install dependencies:** Create a virtual environment and install the required libraries using the requirements.txt file:<br>
pip install -r requirements.txt <br>
3. **Set up your OpenWeatherMap API key:**<br>
- Sign up at OpenWeatherMap and get your API key.<br>
- Replace YOUR_API_KEY in fetch_aqi.py with your actual API key.<br>
4. **Run the Flask application:** python src/app.py<br>
5. **Access the application:** Open a web browser and go to http://127.0.0.1:5000/ to see the real-time air quality data.<br>
## Screenshots 🖺 <br>
![image](https://github.com/user-attachments/assets/19db1f2b-5c7b-41ff-805f-9aece8526f5b)

### For Kolkata,West Bengal,India<br>
![image](https://github.com/user-attachments/assets/3c841461-547b-4a35-87ca-23852b88d6d0)

### For Arnstein,Germany<br>
![image](https://github.com/user-attachments/assets/b3cc1fa9-a584-493f-a4f6-194a45528926)

# Contributing 🟩<br>
- **Fork the repository ➡️ Create a new branch (git checkout -b feature-branch)➡️ Commit your changes (git commit -m 'Add new feature')➡️Push to the branch (git push origin feature-branch)➡️ Open a pull request.**
- For changing locations alter the latitude & longitude value in src/app.py -> save -> (run in terminal) python src/app.py 

# License :
**This project is licensed under the MIT License - see the LICENSE file for details**.<br>

