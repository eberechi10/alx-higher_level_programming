#!/bin/bash
# script to send request to URL using curl, displays size of body
curl -s "$1" | wc -c
