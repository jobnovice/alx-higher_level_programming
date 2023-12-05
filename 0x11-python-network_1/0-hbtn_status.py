#!/usr/bin/python3
# a scirpt that fetches a given URL
import urlib.request
with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    the_page = response.read()
    