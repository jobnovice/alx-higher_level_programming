#!/bin/bash
# sends a request to a given url and prints the response body
curl -sI $1 | grep Content-Length | cut -d " " -f2