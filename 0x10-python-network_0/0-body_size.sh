#!/bin/bash
#a bash script that accepts a URL
curl -sI "$1" | grep -i content-length | cut -d " " -f2"
