#!/usr/bin/python3
"""
    This script fetches last 10 github commits
    of a repository and print it in format
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 3:
        print('Usage: <script> <repo_name> <username>')
    else:
        owner = sys.argv[2]
        username = sys.argv[1]
        url = f'https://api.github.com/repos/{owner}/{username}/commits?per_page=10'
        response = requests.get(url)
        for resp in response.json():
            print('{}: {}'.format(resp.get('sha'),
                                  resp.get('commit').get('author').get('name')))
