#!/usr/bin/python3
# a python script that takes a url as an argument and prints a variable
import urllib.request
import sys
rs = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(rs) as reponse:
    print(reponse.headers['X-Request-Id'])
