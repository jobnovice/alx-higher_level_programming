#!/bin/bash
#provide the list of all available methods the server can accept
curl -si $1 | grep Allow | cut -d ' ' -f2
