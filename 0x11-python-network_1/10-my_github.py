#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    header = {
            "Authorization": 'Bearer ' + argv[2],
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    response = requests.get(url, headers=header)
    print(response.json().get('id'))
