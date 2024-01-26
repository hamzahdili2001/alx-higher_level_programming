#!/usr/bin/python3
"""script that list 10 commits (from the most recent to oldest)"""
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    github_url = "https://api.github.com/repos/{}/{}/commits".format(
        repository_name, owner_name
    )
    req = requests.get(github_url)
    commits = req.json()
    for commit in commits[:10]:
        print(
            "{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name"),
            )
        )
