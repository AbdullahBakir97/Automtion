import os

def generate_directory_structure(root_dir, indent=''):
    structure = []
    items = os.listdir(root_dir)
    items.sort()  # Sort items to maintain consistent order

    for index, item in enumerate(items):
        full_path = os.path.join(root_dir, item)
        is_last = index == len(items) - 1
        marker = '└── ' if is_last else '├── '
        structure.append(f"{indent}{marker}{item}")

        if os.path.isdir(full_path):
            if is_last:
                structure.extend(generate_directory_structure(full_path, indent + '    '))
            else:
                structure.extend(generate_directory_structure(full_path, indent + '│   '))

    return structure

def write_directory_structure_to_file(root_dir, output_file):
    structure = generate_directory_structure(root_dir)
    with open(output_file, 'w', encoding='utf-8') as file:
        try:
            file.write("\n".join(structure))
        except UnicodeEncodeError:
            print("Error: Unable to write some characters to the file. Check your encoding settings.")

# Example usage
if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))  # The directory where this script is located
    output_file = os.path.join(root_directory, 'directory_structure.txt')

    write_directory_structure_to_file(root_directory, output_file)
    print(f"Directory structure written to {output_file}")
