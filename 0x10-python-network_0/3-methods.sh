#!/bin/bash
#provide the list of all available methods the server can accept
curl -sI "$1" | grep Allow | cut -d " " -f2-
