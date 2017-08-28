# Holberton School - 0x11. Python - Network #1

## Description

The focus of this project is to learn:
* how to fetch internet resources with the Python package urllib
* how to decode urllib body response
* how to use the Python package requests #requestsiswaysimplerthanurllib
* how to make HTTP GET request
* how to make HTTP POST/PUT/etc. request
* how to fetch JSON resources
* how to manipulate data from an external service

## Environment
* __Environment:__ Ubuntu 14.04 LTS
* __Python3 version:__ 3.4.3
* __Python style:__ PEP 8

## Helpful Links
* <a href="https://docs.python.org/3/howto/urllib2.html">HOWTO Fetch Internet Resources Using urllib Package</a>
* <a href="http://docs.python-requests.org/en/master/user/quickstart/">Quickstart with Requests package</a>
* <a href="http://docs.python-requests.org/en/master/">Requests package</a>

## File Descriptions
`0-hbtn_status.py`: fetches https://intranet.hbtn.io/status.
`1-hbtn_header.py`: takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
`3-error_code.py`: takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
`4-hbtn_status.py`: fetches https://intranet.hbtn.io/status
`5-hbtn_header.py`: takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
`6-post_email.py`: takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
`7-error_code.py`: takes in a URL, sends a request to the URL and displays the body of the response.
`8-json_api.py`: takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
`9-starwars.py`: sends a search request to the Star Wars API
`10-my_github.py`: takes your Github credentials (username and password) and uses the Github API to display your id

## Author
Stuart Kuredjian

twitter: @stueygk

linkdin: https://www.linkedin.com/in/stuart-kuredjian-8100a273/

## License
Public Domain, no copyright protection