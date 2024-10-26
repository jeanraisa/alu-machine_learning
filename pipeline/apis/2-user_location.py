#!/usr/bin/env python3
"""
Prints the location of a GitHub user specified
as an argument to the script.
"""

import sys
import requests
import json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <github_username>")
        sys.exit(1)

    username = sys.argv[1]
    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP codes 4xx or 5xx

        data = response.json()
        location = data.get('location', 'Location not available')
        print(location)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 403:
            print("Rate limit exceeded. Please try again later.")
        elif response.status_code == 404:
            print("User not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

