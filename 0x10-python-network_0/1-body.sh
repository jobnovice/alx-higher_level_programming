#!/bin/bash
# sends a GET request for a given url and returns the reposne body only if the http status coed is 200
curl -sIX "GET" $1 | awk '/^HTTP/ {print $2}'