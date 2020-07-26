import os
import json
import requests


url1 = 'https://api.github.com/users/GefMar'

response = requests.get(url1)
data = response.json()
print(1)
