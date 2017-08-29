#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""


def main():
    """ Entry point """
    import requests
    from sys import argv

    query = argv[1]
    search_url = 'https://swapi.co/api/people/?search={}'.format(query)
    r = requests.get(search_url)
    json = r.json()
    results = json.get('results')
    names = []
    print('Number of results: {}'.format(json.get('count')))
    for result in results:
        print(result['name'])

if __name__ == '__main__':
    main()
