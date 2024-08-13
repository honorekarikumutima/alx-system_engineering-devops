#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of total
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the
        request fails or the subreddit does not exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "nabuntu_bot-01"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=60)
        response.raise_for_status()
        data = response.json()

        return data.get("data", {}).get("subscribers", 0)

    except requests.RequestException:
        return 0
