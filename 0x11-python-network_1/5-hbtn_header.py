#!/usr/bin/python3
"""
    This script takes a url as argument and sends
    a request to the url, then get the X-Request-Id
    header
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print('Usage: <script> <url>')
    else:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
