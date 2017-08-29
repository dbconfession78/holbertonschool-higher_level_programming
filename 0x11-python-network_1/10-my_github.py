#!/usr/bin/python3
"""
takes your Github credentials (username and password)
and uses the Github API to display your id
"""


def main():
    """ Entry point """
    import requests
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    try:
        print(r.json()['id'])
    except:
        print(None)

if __name__ == '__main__':
    main()
