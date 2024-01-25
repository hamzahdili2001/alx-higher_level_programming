#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# size must be displayed in bytes

curl -sfI "$1" | grep 'Content-Length' | cut -d " " -f2
