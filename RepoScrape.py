import requests
import json

# Prompt the user for a search query
query = input("Enter your search query: ")

# Send a GET request to the GitHub Search API
response = requests.get(f"https://api.github.com/search/repositories?q={query}")

# Parse the search results as a JSON object
results = response.json()

# Find all of the repository links in the search results
repo_links = [repo["html_url"] for repo in results["items"]]

# Filter the repository links to only include those that point to github.com
github_links = [link for link in repo_links if "github.com" in link]

# Print the github links
for link in github_links:
    print(link)
