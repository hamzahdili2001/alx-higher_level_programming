#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8)."""
import sys
import urllib.request

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
