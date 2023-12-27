import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print('Welcome to the organize.py script - happy clean folder')

for filename in os.listdir(current_dir):
    file_path = os.path.join(current_dir, filename)

    # Get the file extension using os.path.splitext
    _, file_extension = os.path.splitext(filename)

    if file_extension.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
        destination_folder = 'Images'
    elif file_extension.lower() in ['.css', '.html', '.js', '.bash']:
        destination_folder = 'Codes'
    elif file_extension.lower() in ['.mp4', '.webm']:
        destination_folder = 'Videos'
    elif file_extension.lower() in ['.pdf', '.word']:
        destination_folder = 'Docs'
    elif file_extension.lower() in ['.winrar', '.zip', '.archive', '.tar']:
        destination_folder = 'Archives'
    elif file_extension.lower() in ['.dmg', '.exe']:
        destination_folder = 'Apps'
    elif file_extension.lower() in ['.chrome', '.firefox']:
        destination_folder = 'Web'
    else:
        # Skip files with unknown extensions
        continue

    # Create the destination folder if it doesn't exist
    destination_path = os.path.join(current_dir, destination_folder)
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    # Move the file to the destination folder
    shutil.move(file_path, os.path.join(destination_path, filename))
    print(f'{filename} moved to {destination_folder} folder')
