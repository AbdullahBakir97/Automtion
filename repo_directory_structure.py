import os
import requests

# GitHub API endpoint for repository contents
github_api_url = "https://api.github.com/repos/{owner}/{repo}/contents/{path}"

def extract_github_details(repo_url):
    # Example repo_url: https://github.com/username/repository-name/tree/branch/path
    parts = repo_url.rstrip('/').split('/')
    owner = parts[3]
    repo = parts[4]
    path = '/'.join(parts[6:]) if len(parts) > 6 else ''
    return owner, repo, path

def fetch_directory_structure_from_github(owner, repo, path='', access_token=None, indent=''):
    headers = {}
    if access_token:
        headers['Authorization'] = f"token {access_token}"

    url = github_api_url.format(owner=owner, repo=repo, path=path)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contents = response.json()

        structure = []

        # Sort contents by type (directories first, then files)
        contents.sort(key=lambda x: (x['type'], x['name']))

        for index, item in enumerate(contents):
            is_last = index == len(contents) - 1
            prefix = '└── ' if is_last else '├── '

            if item['type'] == 'dir':
                structure.append(f"{indent}{prefix}{item['name']}/")
                structure.extend(fetch_directory_structure_from_github(owner, repo, item['path'], access_token, indent + '│   '))
            elif item['type'] == 'file':
                structure.append(f"{indent}{prefix}{item['name']}")

        return structure
    else:
        raise ValueError(f"Failed to fetch directory structure: {response.status_code} - {response.json().get('message', 'Unknown error')}")

def write_directory_structure_to_file(structure, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(structure))

# Example usage
if __name__ == "__main__":
    # Prompt user for GitHub repository URL
    repo_url = input("Enter GitHub repository URL (e.g., https://github.com/owner/repo): ").strip()

    try:
        # Extract GitHub details from URL
        github_owner, github_repo, github_path = extract_github_details(repo_url)

        # Prompt user for GitHub access token
        access_token = input("Enter GitHub access token (press Enter if none): ").strip()

        # Output file name based on repository name
        output_file = f"{github_repo}_directory_structure.txt"

        # Fetch directory structure from GitHub
        structure = fetch_directory_structure_from_github(github_owner, github_repo, github_path, access_token)
        
        # Write directory structure to file
        write_directory_structure_to_file(structure, output_file)
        print(f"Directory structure written to {output_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to GitHub API - {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"Error: An unexpected error occurred - {ex}")
