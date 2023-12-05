#!/usr/bin/python3
# a script that takes url as argument and print the reponse header
import urllib.request
import sys
rs = sys.argv[1]
with urllib.request.urlopen(rs) as reponse:
    print(reponse.headers['X-Request-Id'])
