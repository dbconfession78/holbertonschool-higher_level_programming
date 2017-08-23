#!/bin/bash
# sends POST request with file contents in json format as param
curl -s "$1" -H "Content-Type: application/json" -X 'POST' -T "$2"
