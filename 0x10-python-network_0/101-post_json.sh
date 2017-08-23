#!/bin/bash
curl -H "Content-Type: application/json" -s -X 'POST' -T "$2" "$1"
