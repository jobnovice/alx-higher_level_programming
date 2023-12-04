#!/bin/bash
# sends a GET request for a given url and returns the reposne body only if the http status
curl -sfL "$1" -X GET
