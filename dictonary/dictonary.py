import json
from functions import fileExistCheck, addDataFile

def main():
    """
    Main function to run the dictionary translation program.
    This function checks if the data file exists, loads the data, and then enters a loop where it prompts the user to enter a word to translate from English. If the word is found in the dictionary, it prints the translation. If the word is not found, it prompts the user to provide a translation and adds it to the dictionary.
    The loop continues until the user enters a blank text, which exits the program.
    Example:
        Enter a word to translate (English) (blank text will exit from dictonary): cat
        The translation of 'cat' is 'kissa'.
        Enter a word to translate (English) (blank text will exit from dictonary): 
    """
    file = 'data.json'
    data = fileExistCheck(file)
    
    while True:
        word = input("Enter a word to translate (English) (blank text will exit from dictonary): ").strip().lower()
        
        if word == "":
            print("Exiting the dictionary.")
            break
        
        translation = data.get(word)
        
        if translation:
            print(f"The translation of '{word}' is '{translation}'.")
        else:
            print(f"'{word}' not found in the dictionary.")
            new_translation = input(f"'{word}' not found. Please provide a translation: ").strip()
            data[word] = new_translation
            
            with open(file, 'w') as file:
                try:
                    json.dump(data, file, indent=4)
                except IOError:
                    print("Could not open file. Using default dictionary.")
                    data = {
                        "cat": "kissa",
                        "dog": "koira",
                        "horse": "hevonen"
                    }
                    print("Using default dictionary:", data)
            
            if addDataFile('data.json', data):
                print(f"'{word}' has been added to the dictionary with the translation '{new_translation}'.")
            else:
                print(f"Failed to add '{word}' to the dictionary.")

if __name__ == "__main__":
    main()