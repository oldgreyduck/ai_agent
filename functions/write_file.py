import os
from google import genai
from google.genai import types


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
   
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
) 
