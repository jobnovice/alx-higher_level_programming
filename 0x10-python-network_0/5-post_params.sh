#!/bin/bash
#another request from us to the server with a few variables sent along with
curl -sH $1 -X POST "email: test@gmail.com" -H "subject: I will always be here for PLD" 
