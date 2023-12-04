#!/bin/bash
#another request from us to the server with a few variables sent along with
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1 -X POST 
