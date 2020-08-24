# -*- coding: utf-8 -*-
import requests

URL = "http://127.0.0.1:5000/"
data = [{
    "name": "Abdessalam",
    "lastname": "Zaimi",
    "street": "4 rue Pasteur",
    "city": "Paris",
    "zipcode": 94270,
    "state": "France",
    "parent1_id": 0,
    "parent2_id": 0
}]

print("test : add complete user data")
response = requests.put(URL + "user/", data[0])
print(response)

print("----------")
print("test : get existing user data")
response = requests.get(URL + "user/")
print(response)


