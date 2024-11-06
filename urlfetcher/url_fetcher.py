from functions import load_url, check_url, count_words, save_content
import re

def get_user_input(prompt):
    return input(prompt)

def main():
    """
    Main function to fetch and process a URL provided by the user.
    This function performs the following steps:
    1. Prompts the user to input a URL.
    2. Validates the URL and checks its content type.
    3. Loads the content from the URL.
    4. If the content is HTML, it removes HTML tags and counts the number of dangerous words.
    5. Prompts the user to input a file path to save the content.
    6. Saves the content to the specified file path.
    Example:
        >>> main()
        Give me a valid URL to download? https://example.com
        Number of dangerous words: 5
        Give me a valid path to save the contents? /path/to/save
    Raises:
        Exception: If any error occurs during the URL fetching or processing.
    """
    url = get_user_input("Give me a valid URL to download? ")
    is_valid, content_type = check_url(url)
    if not is_valid:
        print("Invalid URL or the site does not exist.")
        return
    try:
        content = load_url(url, binary=content_type == 'image/jpeg')
        if content is None:
            print("Failed to load the URL.")
            return
        if content_type == 'text/html':
            try:
                text_content = re.sub('<[^<]+?>', '', content)  # Remove HTML tags
                dangerous_word_count = count_words(text_content)
                print(f"Number of dangerous words: {dangerous_word_count}")
            except UnicodeDecodeError:
                print("The content is not a valid UTF-8 encoded HTML file.")
        path = get_user_input("Give me a valid path to save the contents? ")
        if content_type == 'image/jpeg':
            path += '.jpg'
        is_binary = content_type == 'image/jpeg'
        save_content(content, path, is_binary=is_binary)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
