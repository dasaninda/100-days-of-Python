import requests


account_SID = "AC3743a65d0a35ea194d8946ce546f6c15"
auth_token = "1d2b5e2bf5b8a223eff7ba6c5b0310cd"
twilio_phn_number = "+15075568826"

api_key = "b7e7a201146d5fa841b57e5a6dd26c05"
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params= {
"lat": 43.774578,
"lon": -79.252357,
"appid": api_key,
}

response = requests.get(api_endpoint, params= weather_params)

print(response.json())

