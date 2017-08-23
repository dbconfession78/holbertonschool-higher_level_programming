#!/bin/bash
# displays the allowable request types of a server
curl -sI "$1" | grep Allow | cut -d':' -f2 | cut -c 2-
