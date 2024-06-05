#!/usr/bin/python3
"""making a request to reddit api documentation for"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of the subcribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return 0
        res = response.json()
        return [res['data']['subscribers']]
    except requests.exceptions.RequestException as e:
        return 0
