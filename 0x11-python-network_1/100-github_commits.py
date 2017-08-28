#!/usr/bin/python3
"""
takes github repository name and owner to display 10 most recent commits
"""
import requests
from sys import argv

repo = argv[1]
owner = argv[2]
url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
r = requests.get(url, auth=('dbconfession78', 'Hyrenkosa1'))
results = r.json()
for i, result in enumerate(results):
    if i < 10:
        sha = result['sha']
        author = result['commit']['author']['name']
        print('{}: {}'.format(sha, author))
    else:
        break
