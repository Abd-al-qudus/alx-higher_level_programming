#!/usr/bin/python3
"""
    This script takes in a message in the variable q
    and sends a post request to the url then print
    the body as response in formatted ways
"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    arg = "" if not sys.argv[1] else sys.argv[1]
    response = requests.post(url, data={'q': arg})
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
