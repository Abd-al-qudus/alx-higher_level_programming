#!/usr/bin/python3

"""This module sends http request to the alx
    status page @ https://alx-intranet.hbtn.io/status
    and prints the response ina body format"""

if __name__ == "__main__":
    import urllib.request

    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f'\t- type: {type(body)}')
        print(f'\t- content: {body}')
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
