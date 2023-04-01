#!/usr/bin/python3
"""
    This script takes two argument
        url - url to send email to
        email - email to send
    and send email to the url using request library
"""

if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) != 3:
        print('Usage: <script> <url> <email>')
    else:
        response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print('Your email is: {}'.format(response.text))
