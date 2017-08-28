#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import requests
from sys import argv

url = 'http://0.0.0.0:5000/search_user'
param1 = ""

if (len(argv) == 2):
    param1 = argv[1]

payload = {
    'q': param1
}
r = requests.post(url, data=payload)
try:
    json = r.json()
    if (len(json) == 0):
        print('No result')
    else:
        _id = json.get('id')
        name = json.get('name')
        print('[{}] {}'.format(_id, name))
except:
    print('Not a valid JSON')
