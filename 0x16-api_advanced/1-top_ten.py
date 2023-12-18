#!/usr/bin/python3
"""
Reddit API Top Ten Posts Viewer

This script queries the Reddit API and prints the titles of the first ten hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first ten hot posts for a specified subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints the post titles or "None" if an error occurs.
    """
    posts = ""
    if not isinstance(subreddit, str):
        posts = "None\n"
    else:
        api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'safari:holberton/0.1.0'}
        response = requests.get(api_url, headers=headers)
        if response.status_code != 200:
            posts = "None\n"
        else:
            posts_json = response.json().get("data").get("children")
            for i in range(10):
                post_title = posts_json[i].get("data").get("title")
                posts += "{}\n".format(post_title)
    print(posts, end="")
