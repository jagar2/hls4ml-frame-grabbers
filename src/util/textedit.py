def replace_line(file_path, line_start, new_line):
    """
    Replaces the specific line in CustomLogic.h that contains the placeholder comment with the new stripe order array.

    Args:
        file_path (str): The path to the CustomLogic.h file.
    """

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the line
    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(line_start):
                file.write(new_line + "\n")
                print(f"{line} replaced with {new_line}")
            else:
                file.write(line)
                

def multiline_replace_line(file_path, target_line, replacement_lines):
    """
    Replaces a specific line in a file with a list of strings.

    Args:
        file_path (str): Path to the file to be modified.
        target_line (str): The exact line in the file to be replaced.
        replacement_lines (list): List of strings where each entry is a new line to replace the target line.
    """
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if the target line exists in the file
    target_exists = any(line.strip() == target_line.strip() for line in lines)

    # If the target line exists, replace it with the replacement lines
    if target_exists:
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() == target_line.strip():
                    for replacement_line in replacement_lines:
                        file.write(replacement_line + '\n')
                else:
                    file.write(line)
    else:
        # If the target line does not exist, do nothing (pass)
        pass
                
def replace_lines_in_file(file_path, start_marker, end_marker, replacement_lines):
    """
    Replaces the lines between specified start and end markers in a file with a list of strings.

    Args:
        file_path (str): Path to the file to be modified.
        start_marker (str): The line marking the start of the section to be replaced.
        end_marker (str): The line marking the end of the section to be replaced.
        replacement_lines (list): List of strings where each entry is a new line to replace the section.
    """
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the start and end positions of the section to replace
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if start_marker.strip() in line.strip():
            start_idx = i
        if end_marker.strip() in line.strip():
            end_idx = i
            break

    # Check if both markers were found
    if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
        # Keep lines before start marker, add replacement lines, and then keep lines after end marker
        new_lines = lines[:start_idx + 1]  # Keep the start marker line
        new_lines.extend([f'    {rl}\n' for rl in replacement_lines])  # Add replacement lines with indentation
        new_lines.extend(lines[end_idx:])  # Keep the end marker line and lines after it

        # Write the new content back to the file
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
    else:
        # If either start or end marker is not found, do nothing
        pass
