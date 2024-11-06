import os

def save_content(content, path, is_binary=True):
    """
    Save the given content to a specified file path.
    Parameters:
    content (bytes or str): The content to be saved. Should be bytes if is_binary is True, otherwise a string.
    path (str): The file path where the content should be saved.
    is_binary (bool): Flag indicating whether the content is binary (True) or text (False). Default is True.
    Raises:
    ValueError: If the file extension does not match the content type.
    Exception: If there is an error during the file saving process.
    Example:
    >>> save_content(b'binary content', 'example.bin', is_binary=True)
    Saving succeeded to: example.bin
    >>> save_content('text content', 'example.txt', is_binary=False)
    Saving succeeded to: example.txt
    """
    try:
        _, ext = os.path.splitext(path)
        if (is_binary and ext not in ['.jpg', '.png', '.bin']) or (not is_binary and ext not in ['.txt', '.html']):
            raise ValueError("File extension does not match content type.")
        
        mode = 'wb' if is_binary else 'w'
        encoding = None if is_binary else 'utf-8'
        with open(path, mode, encoding=encoding) as file:
            if is_binary:
                file.write(content if is_binary else content.decode('utf-8'))
            else:
                file.write(content)
        print(f"Saving succeeded to: {path}")
    except Exception as e:
        print(f"Error saving file: {e}")

# Example usage:
# save_content(b'binary data', 'path/to/binaryfile.jpg', is_binary=True)
# save_content('text data'.encode('utf-8'), 'path/to/textfile.txt', is_binary=False)