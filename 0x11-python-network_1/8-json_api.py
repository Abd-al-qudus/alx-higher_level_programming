#!/usr/bin/python3
"""
    This script takes in a message in the variable q
    and sends a post request to the url then print
    the body as response in formatted ways
"""

if __name__ == '__main__':
    import sys
    import requests

    q = ''
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1]:
        q = sys.argv[1]
    response = requests.post(url, data={'q': q})
    if response.json() != {}:
        print('[{}] {}'.format(response.json().get('id'), response.json().get('name')))
    elif not response.json():
        print('Not a valid JSON')
    else:
        print('No result')
