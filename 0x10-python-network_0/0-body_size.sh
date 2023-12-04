#!/bin/bash
# sends a request to a given url and prints the response body size
curl -sI $1 | grep Content-Length | cut -d " " -f2
