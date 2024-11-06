import os
import json
import sys

class FileError(Exception):
    pass

def fileExistCheck(file_path):
    """
    Checks if a file exists at the given file path. If the file does not exist, it creates the necessary directories and uses a default dictionary.
    If the file exists, it loads the dictionary from the file. If the file is corrupted, it exits gracefully.
    
    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        dict: The dictionary loaded from the file or the default dictionary if the file does not exist.
    
    Example:
        data = fileExistCheck('/path/to/dictionary.json')
    """
    # Ensure the directory exists
    dir_name = os.path.dirname(file_path)
    if dir_name:
        try:
            os.makedirs(dir_name, exist_ok=True)
        except OSError as e:
            raise FileError(f"Error: Invalid directory name {dir_name}. {e}")

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Could not open file. Using default dictionary.")
        data = {
            "cat": "kissa",
            "dog": "koira",
            "horse": "hevonen"
        }
        print(f"Using default dictionary: words ({', '.join(data.keys())})")
    else:
        print(f"{file_path} already exists, using data.")
        # Load the existing dictionary from the file
        data = None
        try:
            with open(file_path, 'r') as file:
                if os.stat(file_path).st_size == 0:
                    raise FileError(f"Error: {file_path} is empty.")
                data = json.load(file)
            print(f"Loaded dictionary from file {file_path}")
        except json.JSONDecodeError:
            print(f"Error: {file_path} is corrupted. Exiting program...")
            sys.exit()  # Exit the program silently without raising further errors
        except FileError as e:
            print(e)
            sys.exit()  # Exit on file errors silently

    return data
