#!/bin/bash
#sends POST request with file contents in json format as param
curl -H "Content-Type: application/json" -sX POST -T "$2" "$1"
