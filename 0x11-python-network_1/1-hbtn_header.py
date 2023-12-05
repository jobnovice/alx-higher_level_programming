#!/usr/bin/python3
"""a script that takes a url as an argument and prints the response header"""
import urllib.request
import sys
rs = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(rs) as reponse:
    print(reponse.headers['X-Request-Id'])
