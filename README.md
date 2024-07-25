# NeoMoweather

## Introduction
NeoMoweather is a sleek and modern weather application that fetches weather data using the AccuWeather API and presents it with a neomorphic design. The application aims to provide users with an aesthetically pleasing and user-friendly interface to check the weather conditions.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To install and run the NeoMoweather application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/neomoweather.git
   cd neomoweather
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a .env file in the root directory of the project.
   - Add your AccuWeather API key to the .env file :
     ```bash
     API_KEY=your_accuweather_api_key
     ```
## Usage
To run the application, use the following command:
```bash
python app.py
```
Open your web browser and go to http://localhost:5000 to view the application.

## Features
   - Fetches current weather data from the AccuWeather API.
   - Displays weather conditions with a modern neomorphic UI.
   - Responsive design for better user experience on different devices.
   - Includes additional weather information such as temperature, condition, and location.
## Dependencies
   - Flask: A micro web framework for Python.
   - Requests: A simple, yet elegant HTTP library.
   - Python-dotenv: A library to read key-value pairs from a .env file and set them as environment variables.

## Configuration
Ensure your .env file contains the following environment variable:
```bash
API_KEY=your_accuweather_api_key
```
## Documentation
### API Key Configuration
To use the AccuWeather API, you need an API key. You can get one by signing up on the AccuWeather website. Once you have the API key, add it to your .env file as described in the Configuration section.

### File Structure
- app.py: The main application file that contains the logic for fetching weather data and - 
  rendering the UI.
- styles.css: Contains the CSS for the neomorphic design of the UI.
- .env: Contains the environment variables, specifically the AccuWeather API key.
### Key Components
    - app.py: This file contains the Flask application setup and the route to fetch and display weather data.
    - styles.css: This file contains the styling for the neomorphic UI, including classes for different elements such as the weather card, temperature display, and more.

## Examples
Here are some examples of how the application looks and works:

    = Enter a location in the search bar to get the current weather conditions.
    - The weather card will display the temperature, condition, and location with a modern neomorphic design.
## Troubleshooting
If you encounter any issues, consider the following troubleshooting steps:

    - Ensure that your AccuWeather API key is correctly set in the .env file.
    - Check if all required dependencies are installed by running pip install -r requirements.txt.
    - Verify that the Flask server is running and accessible at http://localhost:5000.
## Contributors
    - Sayan Golder(#sayangolder2004@gmail.com) 
## License
This project is licensed under the MIT License.


   
   
