#!/bin/bash
#sending a custom header variable
curl -sH "X-School-User-Id: 98" "$1"
