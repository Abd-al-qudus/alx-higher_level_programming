#!/usr/bin/python3
"""
    This script fetches the response by sending
    a request to the url argument with request library
    and prints the response in body format
"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
