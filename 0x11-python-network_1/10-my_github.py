#!/usr/bin/python3
"""
    this script takes a github username and password
    and login with basic authentication
"""

if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    if len(sys.argv) != 3:
        print('Usage: <script> <username> <password>')
    else:
        github = 'https://api.github.com/user'
        username = sys.argv[1]
        password = sys.argv[2]
        auth = HTTPBasicAuth(username=username, password=password)
        response = requests.get(github, auth=auth)
        print(response.json().get('id'))
