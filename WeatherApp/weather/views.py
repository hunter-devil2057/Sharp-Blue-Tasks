from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json, requests

# Create your views here.
def weather(request):
    # Fetching the data using our WeatherAPI
    # form bata data pathauna laii: POST gareko ho
    # page herna/request garna pareko vaye: GET use hunthiyo

    if request.method == 'POST':
        city = request.POST['city']

        # API key is coming from .env through settings.py
        api_key = settings.OPENWEATHER_API_KEY

        # Using the city entered by the user
        source = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}"
        )
        response = requests.get(source)
        list_of_data = response.json()
        # Checking if city was found
        if response.status_code != 200:
            data = {
                'error': list_of_data.get(
                    'message',
                    'City not found'
                )
            }
            return render(request, "weather.html", data)

        data = {
            'coordinate': (str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])),
            'weather_id': str(list_of_data['weather'][0]['id']),
            'weather_main': str(list_of_data['weather'][0]['main']),
            'weather_description': str(list_of_data['weather'][0]['description']),
            'weather_icon': str(list_of_data['weather'][0]['icon']),
            'country_code': str(list_of_data['sys']['country']),
            'temp': round(list_of_data['main']['temp'] - 273.15, 2),
            'feels_like': round(list_of_data['main']['feels_like'] - 273.15, 2),
            'temp_min': round(list_of_data['main']['temp_min'] - 273.15, 2),
            'temp_max': round(list_of_data['main']['temp_max'] - 273.15, 2),
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            # These values may not exist for every location
            'sea_level': str(list_of_data['main'].get('sea_level', 'N/A')),
            'ground_level': str(list_of_data['main'].get('grnd_level', 'N/A')),
            'visibility': str(list_of_data.get('visibility', 'N/A')),
            'wind_speed': str(list_of_data['wind'].get('speed', 'N/A')),
            'wind_direction': str(list_of_data['wind'].get('deg', 'N/A')),
            'wind_gust': str(list_of_data['wind'].get('gust', 'N/A')),
            # Rain may not exist if there is no rain
            'rain': str(list_of_data.get('rain', {}).get('1h', 'N/A')),
            'cloudiness': str(list_of_data['clouds'].get('all', 'N/A')),
            'city_id': str(list_of_data['id']),
            'city_name': str(list_of_data['name']),
            'timezone': str(list_of_data['timezone']),
            'sunrise': str(list_of_data['sys']['sunrise']),
            'sunset': str(list_of_data['sys']['sunset']),
            'cod': str(list_of_data['cod'])
        }

    else:
        data = {}

    return render(request, "weather.html", data)