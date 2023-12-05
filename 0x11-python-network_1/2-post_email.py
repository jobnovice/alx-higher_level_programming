#!/usr/bin/python3
# a python script that takes a url as an argument

if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))