import requests

class GitHubClient:
    BASE_URL = 'https://api.github.com'

    def __init__(self, access_token):
        self.access_token = access_token

    def create_repository(self, repo_name):
        url = f'{self.BASE_URL}/user/repos'
        headers = {'Authorization': f'token {self.access_token}'}
        payload = {'name': repo_name, 'private': False}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def create_branch(self, repo_name, branch_name):
        url = f'{self.BASE_URL}/repos/{repo_name}/git/refs'
        headers = {'Authorization': f'token {self.access_token}'}
        payload = {'ref': f'refs/heads/{branch_name}', 'sha': self.get_default_branch_sha(repo_name)}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def create_tag(self, repo_name, branch_name, tag_name):
        url = f'{self.BASE_URL}/repos/{repo_name}/git/refs'
        headers = {'Authorization': f'token {self.access_token}'}
        payload = {'ref': f'refs/tags/{tag_name}', 'sha': self.get_commit_sha(repo_name, branch_name)}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_default_branch_sha(self, repo_name):
        url = f'{self.BASE_URL}/repos/{repo_name}'
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['default_branch']

    def get_commit_sha(self, repo_name, branch_name):
        url = f'{self.BASE_URL}/repos/{repo_name}/commits/{branch_name}'
        headers = {'Authorization': f'token {self.access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['sha']

# Example usage
access_token = 'PeEx_2023'

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
