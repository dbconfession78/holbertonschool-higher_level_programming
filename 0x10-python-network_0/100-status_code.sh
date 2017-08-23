#!/bin/bash
# displays the requests response status code
curl -sIL "$1" -w '%{http_code}' -o /dev/null
