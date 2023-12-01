#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests

if __name__ == '__main__':
    ch = "" if len(argv) == 1 else argv[1]

    values = {'q': ch}
    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data=values)
        json_body = res.json()

        if json_body == {}:
            print('No result')
        else:
            print('{[]} {}'.format(json_body.get('id'), json_body.get('name')))
    except ValueError:
        print('Not a valid JSON')
