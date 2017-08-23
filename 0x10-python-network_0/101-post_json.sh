#!/bin/bash
curl -s "$1" -H "Content-Type: application/json" -X 'POST' -T "$2"
