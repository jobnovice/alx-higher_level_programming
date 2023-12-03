#!/bin/bash
#a bash script that accepts a URL
echo $(curl -sI "$1" | grep Content-Length | cut -d " " -f2")
