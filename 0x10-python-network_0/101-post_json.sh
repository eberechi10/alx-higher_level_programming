#!/bin/bash
# script to sends JSON POST request to  URL, and displays the body.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
