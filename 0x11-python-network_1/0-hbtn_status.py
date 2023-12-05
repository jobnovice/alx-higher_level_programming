#!/usr/bin/python3
# a scirpt that fetches a given URL
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print(response.read())
