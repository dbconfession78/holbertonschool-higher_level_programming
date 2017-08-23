#!/bin/bash
#sends POST request with file contents in json format as param
curl -sH "Content-Type: application/json" -d "@$2" "$1"
