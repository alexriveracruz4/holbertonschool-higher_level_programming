#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge."""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))
