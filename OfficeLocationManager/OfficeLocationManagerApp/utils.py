import requests

def get_current_weather(latitude, longitude):
    url = f'<https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true>'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['current_weather']
    Else:
        return None
