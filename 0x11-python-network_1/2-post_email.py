#!/usr/bin/python3
"""
    This script takes two arguments
        url - send a post request to the yrl
        email: email to post
    and print the response in a body format
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) != 3:
        print('Usage: <module> <url> <email>')
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        data = urllib.parse.urlencode({'email': email})
        request = urllib.request.Request(url, data.encode('ascii'))
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
