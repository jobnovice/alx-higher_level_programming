#!/bin/bash
#another request from us to the server with a few variables sent along with
curl -sH "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
