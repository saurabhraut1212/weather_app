# Weather Application

A Python-based weather application that displays real-time weather information using the OpenWeatherMap API. The application features a clean web interface and provides detailed weather data including temperature, humidity, wind speed, and conditions.

## Features

- Real-time weather data retrieval
- Temperature display in Celsius
- Wind speed information
- Humidity levels
- Weather conditions and descriptions
- Responsive web interface
- Template-based rendering system

## Project Structure

```
weather-app/
├── .env                    # Environment variables configuration
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
├── src/
│   ├── server.py         # HTTP server implementation
│   ├── services/
│   │   └── weather_service.py    # Weather API integration
│   ├── templates/
│   │   ├── base.html     # Base template
│   │   ├── home.html     # Home page template
│   │   └── weather.html  # Weather results template
│   └── utils/
│       └── template_engine.py    # Custom template rendering engine
```

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (get it from [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-app
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
python main.py
```

2. The application will automatically open in your default web browser at `http://localhost:8000`

3. Enter a city name in the search box and click "Get Weather" to see the current weather information

## Features Explained

- **Weather Service**: Integrates with OpenWeatherMap API to fetch real-time weather data
- **Template Engine**: Custom implementation for rendering HTML templates with inheritance support
- **Responsive Design**: Clean and user-friendly interface that works on both desktop and mobile devices
- **Error Handling**: Robust error handling for API requests and invalid inputs

## Development

The application uses a modular structure:

- `server.py`: Handles HTTP requests and routing
- `weather_service.py`: Manages API interactions and data processing
- `template_engine.py`: Provides template rendering functionality
- Templates: Separate HTML files for different views with inheritance

## Error Handling

The application includes error handling for:
- Missing API keys
- Invalid city names
- API request failures
- Server errors

## Security Features

- HTML escaping for user inputs
- Environment variable based configuration
- Input validation

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
