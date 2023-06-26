# GitHub API Interaction Script

The GitHub API Interaction Script is a Python script that utilizes a self-developed client class to interact with the GitHub API. The script provides functionality to create a public repository, create a new remote branch (excluding the default branch), and add a tag to the initial commit of the new branch.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## Usage

1. Obtain a GitHub access token:
   - Go to your GitHub account settings.
   - Navigate to "Developer settings" -> "Personal access tokens".
   - Generate a new token with the necessary permissions (e.g., repo access).
   - Copy the generated access token.

2. Replace `'YOUR_GITHUB_ACCESS_TOKEN'` in the script with your GitHub access token.

3. Run the script:

python github_interaction_script.py


4. Follow the instructions and provide the required input when prompted.

## Script Functionality

The script provides the following functionality through the `GitHubClient` class:

### `GitHubClient`

The `GitHubClient` class encapsulates the operations to interact with the GitHub API. It is initialized with a GitHub access token, which is used for authentication in subsequent API calls.

#### Constructor

```python
def __init__(self, access_token: str)

access_token (str): GitHub access token for authentication.
Methods
create_repository

def create_repository(self, repo_name: str) -> dict

Creates a public repository on GitHub.
Returns the repository data as a dictionary.
create_branch

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a public repository on GitHub.
Returns the repository data as a dictionary.
create_branch

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a new remote branch (excluding the default branch) in the specified repository.
Returns the branch data as a dictionary.

'create_branch'

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a new remote branch (excluding the default branch) in the specified repository.
Returns the branch data as a dictionary.

create_branch

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a new remote branch (excluding the default branch) in the specified repository.
Returns the branch data as a dictionary.
create_tag

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a public repository on GitHub.

Returns the repository data as a dictionary.

create_branch

def create_branch(self, repo_name: str, branch_name: str) -> dict

Creates a new remote branch (excluding the default branch) in the specified repository.
Returns the branch data as a dictionary.

create_tag

def create_tag(self, repo_name: str, branch_name: str, tag_name: str) -> dict

Adds a tag to the initial commit of the specified branch in the repository.

Returns the tag data as a dictionary.

get_default_branch_sha

def get_default_branch_sha(self, repo_name: str) -> str

Retrieves the SHA of the default branch in the specified repository.

Returns the SHA as a string.

get_commit_sha

def get_commit_sha(self, repo_name: str, branch_name: str) -> str

etrieves the SHA of the initial commit in the specified branch of the repository.

Returns the SHA as a string.

Example Usage

access_token = 'YOUR_GITHUB_ACCESS_TOKEN'

client = GitHubClient(access_token)

repo_name = 'example-repo'
repo_data = client.create_repository(repo_name)
print(f'Repository "{repo_name}" created successfully.')

branch_name = 'new-branch'
branch_data = client.create_branch(repo_name, branch_name)
print(f'Branch "{branch_name}" created successfully.')

tag_name = 'v1.0.0'
tag_data = client.create_tag(repo_name, branch_name, tag_name)
print(f'Tag "{tag_name}" created successfully.')


Please note that you can copy and use the entire content above as Markdown.

