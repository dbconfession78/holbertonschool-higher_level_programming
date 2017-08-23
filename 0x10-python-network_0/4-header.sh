#!/bin/bash
# sends GET request with custom header and displays the response body
curl -H "X-HolbertonSchool-User-Id: 98" "$1"
