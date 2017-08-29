#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


def main():
    """ Entry point """
    import urllib.request
    import sys

    URL = sys.argv[1]

    with urllib.request.urlopen(URL) as response:
        print(response.headers['X-Request-Id'])

if __name__ == '__main__':
    main()
