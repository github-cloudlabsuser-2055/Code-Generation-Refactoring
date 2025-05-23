import requests
import csv

url = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}"
api_key = "2bcb59ddc23abaa316491c40068d642f"

# Reemplaza {API key} en la URL con la api_key real
url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)
# Guardar datos relevantes en un archivo CSV
with open('weather_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['timezone', 'lat', 'lon', 'temperature'])
    writer.writerow([
        data.get('timezone'),
        data.get('lat'),
        data.get('lon'),
        data.get('current', {}).get('temp')
    ])

# Mostrar por consola la información solicitada
print(f"Zona horaria: {data.get('timezone')}")
print(f"Latitud: {data.get('lat')}")
print(f"Longitud: {data.get('lon')}")
print(f"Temperatura: {data.get('current', {}).get('temp')}")