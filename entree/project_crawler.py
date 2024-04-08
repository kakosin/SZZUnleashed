import requests
import csv
from dotenv import load_dotenv
import os
import time

# Load Environment Variables
load_dotenv('dev.env')

# Set Variables for your GitHub Advanced Search
# Use https://github.com/search/advanced to test first and use the same text
QUERY = "stars:<20000 forks:>1000 language:TypeScript"
BASE_URL = "https://api.github.com/search/repositories"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
RESULT_PAGES = 10


def get_latest_commit(owner, repo):
    """
    Get the latest commit of a given GitHub repository.

    :param owner: The owner of the repository.
    :param repo: The repository name.
    :return: The latest commit data.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        return commits[0] if commits else None
    else:
        raise Exception(f"Failed to get commits for " +
                        "{owner}/{repo}: {response.content}")


def search_github_repositories(query, sort="stars", order="desc", page=1, per_page=10):
    """
    Search for repositories on GitHub.

    :param query: The search query string.
    :param sort: The field to sort by. One of 'stars', 'forks', or 'updated'.
    :param order: The sort order. One of 'asc' or 'desc'.
    :param per_page: Number of results per page.
    :return: A list of repositories matching the search criteria.
    """
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "page": page,
        "per_page": per_page
    }
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()['items']
    else:
        raise Exception(f"Failed to search repositories: {response.content}")

def write_to_csv(filename, repositories, blacklist, mode='w'):
    """
    Write repository data to a CSV file.

    :param repositories: List of repository data.
    :param mode: File opening mode ('w' for write, 'a' for append).
    """
    with open(filename, mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for repo in repositories:
            owner, repo_name = repo['full_name'].split('/')
            if repo_name in blacklist:
                continue
            latest_commit = get_latest_commit(owner, repo_name)
            writer.writerow([repo['html_url'], latest_commit['sha'] if latest_commit else 'None'])
        print(f"Added {len(repositories)} repositories.")

# for page in range(1, RESULT_PAGES):
#     repositories = search_github_repositories(QUERY, page=page)
#     write_mode = 'w' if page == 1 else 'a'
#     write_to_csv(repositories, mode=write_mode)
#     time.sleep(2.5)
