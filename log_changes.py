import subprocess
import os

def get_git_changes(repo_path, output_file):
    # Navigate to the repository path
    os.chdir(repo_path)
    
    # Get the list of commit hashes
    hashes_command = ['git', 'log', '--pretty=format:%h']
    hashes = subprocess.run(hashes_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.splitlines()

    # Open the output file
    with open(output_file, 'w') as file:
        # Iterate over commit hashes and get the detailed changes for each
        for commit_hash in hashes:
            # Get detailed changes for the commit
            show_command = ['git', 'show', '--no-patch', '--format=%h - %an, %ar : %s', commit_hash]
            commit_info = subprocess.run(show_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
            file.write(commit_info + '\n')
            show_command = ['git', 'show', commit_hash]
            commit_changes = subprocess.run(show_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
            file.write(commit_changes + '\n\n')

    print(f"Changes have been written to {output_file}")

# Set the path to your repository and the desired output file
repo_path = 'C:\\Users\\B\\Project\\bot\\src'  # Replace with the path to your local Git repository
output_file = 'detailed_changes.txt'

get_git_changes(repo_path, output_file)