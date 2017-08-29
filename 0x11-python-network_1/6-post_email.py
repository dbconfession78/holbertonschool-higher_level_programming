#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST
request to the passed URL with the email as a
parameter, and finally displays the body of the response.
"""


def main():
    """ Entry point """
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    payload = {
        'email': email
    }

    r = requests.post(url, data=payload)
    print(r.text)

if __name__ == '__main__':
    main()
