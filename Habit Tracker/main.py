import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()


pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token": "sjnkjasbfiurebgfkrilngfewoinowief",
    "username": "sultan7557",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

response = requests.post(url=pixela_endpoint, json=params)
print(response.text)



pixela_graph_endpoint = "https://pixe.la/v1/users/sultan7557/graphs"
headers = {
    "X-USER-TOKEN": "sjnkjasbfiurebgfkrilngfewoinowief"
}
graph_params = {
    "id": "graph1",
    "name": "Reading Book",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
    "timezone": "Asia/Jakarta",
}


graph_response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)


#now we make a request to add a pixel
headers = {
    "X-USER-TOKEN": "sjnkjasbfiurebgfkrilngfewoinowief"
}

today = dt.datetime(year=2025, month=4, day=28)
add_new_pixel_endpoint = "https://pixe.la/v1/users/sultan7557/graphs/graph1"
add_new_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "70",
}

response = requests.post(url=add_new_pixel_endpoint, json=add_new_pixel_params, headers=headers)
print(response.text)

#now we make a request to update a pixel
headers = {
    "X-USER-TOKEN": "sjnkjasbfiurebgfkrilngfewoinowief"
}

update_pixel_endpoint = "https://pixe.la/v1/users/sultan7557/graphs/graph1/20250428"
update_pixel_params = {
    "quantity": "100",

}

requests.put(url = update_pixel_endpoint, json = update_pixel_params, headers = headers)
print("Pixel updated successfully.")
