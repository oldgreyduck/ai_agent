import os


def write_file(working_directory, file_path, content):
    
    full_path = os.path.join(working_directory, file_path)
    allowed_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(full_path)

    if not target_dir_abs.startswith(allowed_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    try:
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception:
        return f"Error: unable to write contents to file"
