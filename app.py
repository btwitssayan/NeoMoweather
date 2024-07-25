from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
import os

# Load environment variables
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('ACCUWEATHER_API_KEY')

# Initialize Flask app
app = Flask(__name__)

def get_location_key(city_name):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        'apikey': api_key,
        'q': city_name
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            return data[0]['Key']
    return None

def get_weather(location_key):
    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}'
    params = {
        'apikey': api_key,
        'metric': True,
        'details': True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city_name = ''
    error = None

    if request.method == 'POST':
        city_name = request.form['loc']
        location_key = get_location_key(city_name)
        if location_key:
            weather_data = get_weather(location_key)
            if weather_data:
                weather_data = weather_data[0]  # Get the first forecast
            else:
                error = "Could not retrieve weather data."
        else:
            error = "City not found."

    return render_template('index.html', weather=weather_data, city=city_name, error=error)

if __name__ == '__main__':
    app.run(debug=True)
