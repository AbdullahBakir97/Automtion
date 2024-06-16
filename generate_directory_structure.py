import os

def generate_directory_structure(root_dir):
    structure = []

    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            structure.append(f"{sub_indent}{file}")

    return "\n".join(structure)

def write_directory_structure_to_file(root_dir, output_file):
    structure = generate_directory_structure(root_dir)
    with open(output_file, 'w') as file:
        file.write(structure)

# Example usage
if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))  # The directory where this script is located
    output_file = os.path.join(root_directory, 'directory_structure.txt')

    write_directory_structure_to_file(root_directory, output_file)
    print(f"Directory structure written to {output_file}")
