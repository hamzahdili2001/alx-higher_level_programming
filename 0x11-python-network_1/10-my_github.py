#!/usr/bin/python3
""" Python script that takes
your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(user, password))
    print(response.json().get("id"))
