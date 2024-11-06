import json
def addDataFile(fileJson, data):
    """
    Adds data to a JSON file.

    This function writes the provided data to the specified JSON file. If the file does not exist, it will be created.
    If an IOError occurs during the writing process, an error message will be printed and the function will return False.

    Args:
        fileJson (str): The path to the JSON file where data will be written.
        data (dict): The data to be written to the JSON file.

    Returns:
        bool: True if the data was successfully written to the file, False otherwise.

    Example:
        success = addDataFile('data.json', {'key': 'value'})
    """
    print(f"Adding data to {fileJson}")
    with open(fileJson, 'w') as file:
        try:
            json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error writing to file {fileJson}: {e}")
            return False
        return True