import os


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."

    full_path = os.path.join(working_directory, directory)
    allowed_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(full_path)

    if not target_dir_abs.startswith(allowed_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    items = os.listdir(full_path)
    lines = []
    for item in items:
        item_path = os.path.join(full_path, item)
        item_size = os.path.getsize(item_path)
        item_dir = os.path.isdir(item_path)
        item_format = f"- {item}: file_size={item_size}, is_dir={item_dir}"
        lines.append(item_format)
    return "\n".join(lines)

