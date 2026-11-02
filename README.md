# Weather App

A Django app that shows the **current weather** for a list of cities. Add a city by name to see its temperature, conditions and icon from the [OpenWeatherMap API](https://openweathermap.org/current), or remove cities you no longer want to track.

## Running

```bash
python -m venv venv && source venv/bin/activate
pip install django requests
python manage.py migrate
python manage.py runserver      # http://localhost:8000
```

Get a free API key from [openweathermap.org](https://home.openweathermap.org/api_keys) and put it in the request URL in `weather/views.py`.

## Routes

| Path | Description |
|---|---|
| `/` | City list with current weather, plus a form to add a city |
| `/delete/<city_name>/` | Remove a city |

## Tech

Python · Django · requests · OpenWeatherMap API · Bulma CSS
