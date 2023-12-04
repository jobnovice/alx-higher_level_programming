#!/bin/bash
# sendss a GET request for a given url and returns the reposne body only if the http status coed is 200
curl -s -w "\n%{http_code}" "$1" | awk '/^$/{p=0} p; /./{p=1}'
