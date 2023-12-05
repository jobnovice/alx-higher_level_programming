#!/usr/bin/python3
# a scirpt that fetches a given URL
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read().decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- type:", body)
