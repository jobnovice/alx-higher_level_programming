#!/usr/bin/python3
# a scirpt that fetches a given URL
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content_bytes = response.read()
    content_str = content_bytes.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(content_bytes)))
print("\t- content: {}".format(content_bytes))
print("\t- utf8 content: {}".format(content_str))
