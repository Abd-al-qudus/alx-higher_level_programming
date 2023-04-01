#!/usr/bin/python3
"""
    This script takes a url as arg and sends a http request
    to the url and then return the value of X-Request-Id
    int the response header
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    if len(sys.argv) != 2:
        print("Usage: <module> <url>")
    else:
        request_url = sys.argv[1]
        request = urllib.request.Request(request_url)
        with urllib.request.urlopen(request) as response:
            header = response.getheader('X-Request-Id')
            print(header)
