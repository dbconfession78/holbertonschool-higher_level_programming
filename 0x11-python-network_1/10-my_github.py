#!/usr/bin/python3
"""
takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from sys import argv

user = argv[1]
passwd = argv[2]
url = 'https://api.github.com/users/{}'.format(user)
r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, passwd))
json = r.json()
_id = json.get('id')
print(_id)
