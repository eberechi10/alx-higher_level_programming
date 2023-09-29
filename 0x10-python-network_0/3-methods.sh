#!/bin/bash
# script to display all HTTP methods acepted by the server using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
