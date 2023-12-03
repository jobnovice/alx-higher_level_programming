#!/bin/bash
#a bash script that accepts a URL
if [$# -eq 0];then
    echo "Usage: $0 <url>"
    exit 1
fi

url=$1


body_size = $(curl -sI $url | grep -i content-length)
echo "$body_size"