# -*- coding: utf-8 -*-
import requests

URL = "http://127.0.0.1:5000/"

print("----------")
print("test : get existing user data")
response = requests.get(URL + "user/0")
print(response.json())
print("----------")

print("test : get non existing user data")
response = requests.get(URL + "user/999")
print(response.json())
print("----------")

print("test : add existing user data")
response = requests.put(URL + "user/0", {"name" : "super", "lastname": "man", "parent1_id" : "0"})
print(response.json())
print("----------")

print("test : add user data with missing information")
response = requests.put(URL + "user/1", {"name" : "super", "lastname": "man"})
print(response.json())
print("----------")

print("test : add complete user data")
response = requests.put(URL + "user/1", {"name" : "super", "lastname": "man", "parent1_id" : "0"})
print(response.json())
print("----------")

print("test : delete existing user data")
response = requests.delete(URL + "user/1")
print(response)
print("----------")

print("test : delete non existing user data")
response = requests.delete(URL + "user/999")
print(response.json())
print("----------")

