#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)
"""
from urllib import request, error
from sys import argv
if __name__ == "__main__":

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
