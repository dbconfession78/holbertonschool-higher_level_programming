#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


URL = sys.argv[1]

with urllib.request.urlopen(URL) as response:
    html = response.read()
print(response.headers['X-Request-Id'])
