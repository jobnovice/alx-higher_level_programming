#!/bin/bash
# sends a GET request for a given url
curl -sIX "GET" $1 | awk '/^HTTP/ {print $2}'