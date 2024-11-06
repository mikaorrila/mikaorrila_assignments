import re
def count_words(text):
    """
    Count the number of dangerous words in a given text.

    This function searches for specific dangerous words in the input text and returns the count of their occurrences.
    The dangerous words are: "bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism".

    Args:
        text (str): The input text to be analyzed.

    Returns:
        int: The count of dangerous words found in the text.

    Example:
        >>> count_words("There was a bomb threat reported.")
        1
        >>> count_words("The terrorist planned to kill.")
        2
    """
    dangerous_words = ["bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"]
    words = re.findall(r'\b\w+\b', text.lower())
    return sum(word in dangerous_words for word in words)