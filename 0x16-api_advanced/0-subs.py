#!/usr/bin/python3
import requests

"""
Reddit Subreddit Subscribers Query

This script defines a function that queries the Reddit API to retrieve the number
of subscribers for a given subreddit.
"""

def  number_of_subscribers(subreddit_name):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit_name (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the specified subreddit.
    """
    # Construct the URL for the Reddit API endpoint of the specified subreddit
    api_url = f"https://api.reddit.com/r/{subreddit_name}/about"

    # Set a custom User-Agent header to identify the client making the request
    headers = {'User-Agent': 'CustomRedditClient/1.0'}

    # Send an HTTP GET request to the Reddit API
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return 0

    # Parse the JSON response from the API
    response_json = response.json()

    # Check if the "data" key is present in the response
    if "data" in response_json:
        # Return the number of subscribers from the response
        return response_json["data"]["subscribers"]
    else:
        return 0
