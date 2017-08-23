#!/bin/bash
# makes a request PUT request with user_id param and custom header
curl -sLX 'PUT' -d 'user_id=98' -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
