#!/usr/bin/python3
"""
    This script takes a url as argument,
     send a request to the url then return
     the status exception if exist
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    if len(sys.argv) != 2:
        print('Usage: <module> <url>')
    else:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
        finally:
            print(body)
