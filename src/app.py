from flask import Flask, render_template
from fetch_aqi import fetch_aqi

app = Flask(__name__, template_folder='../templates')  # Adjust path as needed
def get_recommendation(aqi_value):
    if aqi_value < 50:
        return "Air quality is good. No precautions needed."
    elif 50 <= aqi_value < 100:
        return "Moderate air quality. Sensitive groups should take precautions."
    else:
        return "Unhealthy air quality! Reduce outdoor exposure."

@app.route("/")
def index():
    aqi = fetch_aqi()
    recommendation = get_recommendation(aqi)
    return render_template("index.html", aqi=aqi, recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)
