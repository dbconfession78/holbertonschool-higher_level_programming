#!/usr/bin/env bash
# displays the value of the 'Content-Length' response header
curl -sI "$1" | grep Content-Length | cut -d' ' -f2

# This will get character count of curl response. Not the most accurate, but
# useful if their is no Content-Length header

# response=$(curl -s $1)
# wc=$(echo $response | wc -c)
# echo $wc
