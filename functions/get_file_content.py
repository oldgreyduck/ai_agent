import os
from google import genai
from google.genai import types


def get_file_content(working_directory, file_path):

    full_path = os.path.join(working_directory, file_path)
    allowed_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(full_path)

    if not target_dir_abs.startswith(allowed_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        has_more = f.read(1)
        if has_more:
            return file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
