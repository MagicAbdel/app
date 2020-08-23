# -*- coding: utf-8 -*-
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "user/1")
print(response.json()) 