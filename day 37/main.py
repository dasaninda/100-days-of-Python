## HTTP:

#POST REQUEST
#GET REQUEST
#PUT REQUEST
#DELETE REQUEST

import requests
from datetime import datetime

token = "hgjflghdfjghdkfjghdkfjgh"
username = "aninda"
PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph2"

user_params ={
   "token": token,
   "username": username,
   "agreeTermsOfService": "yes",
   "notMinor": "yes"  , 
}

# response = requests.post(url = PIXELA_USER_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_USER_ENDPOINT}/{username}/graphs"
graph_config ={
    "X-USER-TOKEN": "",
    "id": GRAPH_ID,
    "name":"Gym",
    "unit": "hour",
    "type": "float",                 
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2023, month=8, day=4)
pixel_creation_endpoint = f"{PIXELA_USER_ENDPOINT}/{username}/graphs/{GRAPH_ID}"
pixel_data ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5",
}

response = requests.post(url =pixel_creation_endpoint, json= pixel_data, headers=headers)
print(response.text)
