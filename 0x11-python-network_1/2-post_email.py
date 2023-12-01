#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request
from sys import argv
from urllib import parse

if __name__ == '__main__':
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        page = response.read()
        print(page)
