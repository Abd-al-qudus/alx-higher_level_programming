#!/usr/bin/python3
"""
    This script sends a request to the url argument
    and print the error status code if exist
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print('Usage: <script> <url>')
    else:
        response = requests.get(sys.argv[1])
        if response.status_code >= 400:
            print(f'Error code: {response.status_code}')
        else:
            print(response.text)
