#!/usr/bin/python3
"""
takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from sys import argv

user = argv[1]
passwd = argv[2]
url = 'https://api.github.com/user'
r = requests.get(url, auth=(user, passwd))
print(r.json()['id'])
