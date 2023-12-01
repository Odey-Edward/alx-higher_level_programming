#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type:", type(the_page))
        print("\t- content:", the_page)
        print("\t- utf8 content:", response.msg)
