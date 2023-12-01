#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) form a repository
"""
from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/'\
            + argv[2] + '/' + argv[1] + '/commits'

    response = requests.get(url)

    array = response.json()

    for i in range(10):
        print(
            array[i].get('sha') + ': '
            + array[i].get('commit')['author']['name'])
