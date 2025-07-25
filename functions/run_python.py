import os
import subprocess
from google import genai
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    
    full_path = os.path.join(working_directory, file_path)
    allowed_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(full_path)

    if not target_dir_abs.startswith(allowed_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    elif not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cmd = ["python", file_path] + args
        result = subprocess.run(
            cmd,
            cwd=working_directory,
            timeout=30,
            capture_output=True,
            text=True,
        )
        if not result.stdout and not result.stderr:
            return f"No output produced."
        
        output = result.stdout + result.stderr
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}\n"
        return output
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",  # This must match what the test expects
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute",
            ),
        },
        required=["file_path"],
    ),
)
