# -*- coding: utf-8 -*-
import requests

BASE = "http://127.0.0.1:5000/"

print("test : get existing user information")
response = requests.get(BASE + "user/0")
print(response.json())
print("----------")

print("test : add user information with missing information")
response = requests.put(BASE + "user/1", {"name" : "super", "lastname": "man"})
print(response.json())
print("----------")

print("test : add correctly user information")
response = requests.put(BASE + "user/1", {"name" : "super", "lastname": "man", "parent1_id" : "0"})
print(response.json())
print("----------")

