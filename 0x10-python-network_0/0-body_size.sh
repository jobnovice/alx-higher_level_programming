#!/bin/bash
#a bash script that accepts a URL
echo = $(curl -sI "$1" | grep -i content-length)
