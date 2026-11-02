# Weather App

A Django app that shows the **current weather** for a list of cities. Add a city by name to see its temperature, conditions and icon from the [OpenWeatherMap API](https://openweathermap.org/current), or remove cities you no longer want to track.

## Running

```bash
python -m venv venv && source venv/bin/activate
pip install django requests
python manage.py migrate
python manage.py runserver      # http://localhost:8000
```

Get a free API key from [openweathermap.org](https://home.openweathermap.org/api_keys) and export it as `OPENWEATHER_API_KEY` (see [Configuration](#configuration)).

## Routes

| Path | Description |
|---|---|
| `/` | City list with current weather, plus a form to add a city |
| `/delete/<city_name>/` | Remove a city |

## Tech

Python · Django · requests · OpenWeatherMap API · Bulma CSS

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |
| `OPENWEATHER_API_KEY` | OpenWeatherMap API key |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
