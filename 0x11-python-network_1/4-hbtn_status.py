#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


def main():
    """ Entry point """
    import requests

    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)

    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == '__main__':
    main()
