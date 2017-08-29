#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""


def main():
    """ Entry point """
    from urllib import request, parse, error
    from sys import argv

    url = argv[1]
    html = ''
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.getcode()))

if __name__ == '__main__':
    main()
