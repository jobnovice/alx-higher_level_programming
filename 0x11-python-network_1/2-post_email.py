#!/usr/bin/python3
# a python script that takes a url as an argument

if __name__ == '__main__':
    import urllib.request
    import sys
    rs = urllib.request.Request(sys.argv[1],data="email:{sys.argv[2]}" , method = "POST")
    with urllib.request.urlopen(rs) as response:
        body = response.read().decode("utf-8")
        print("your email  is: ", body.headers["email"])
