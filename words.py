"""
5.2PP Collection of Strings
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def add_word(word_list: list[str], word: str):
    """
    Adds a new word to the word list if there is capacity and
    the word is not empty.

    Args:
        word_list: The list stores words
        word: The new word to add

    Returns: None
    """

    # TODO: Complete the implementation of this function


    if word == "":
        print("Empty word cannot be added to the list")
        
        return


    if word in word_list:
        print("Word already exists.")
    else:
        word_list.append(word)


def display_entries(word_list: list[str]):
    """
    Displays all words in the word list, separated by a comma.

    Returns: None
    """

    # TODO: Complete the implementation of this function
   

    if len(word_list) == 0:
        print("No word to display")
        return
    

    for i, word in enumerate(word_list):
        if i < len(word_list) - 1:
            print(word, end=", ")
        else:
            print(word)


#def main():
    # TODO: Add necessary variable declarations and initialisations
    # TODO: Implement the menu

def average_len(word_list: list[str]) -> float:
    """
    Calculates and returns the average length of all words in the list

    Args:
         word_list: list[str] # the collection of words

    Returns: 
           float: The average lenth of all words in the list word_list.
    """
    
    total : int # total length of all words

    total = 0

    for word in word_list:
        total += len(word)

    return total / len(word_list)


def main():
    """
    Main function controls the driven-menu program.

    Args: None

    Returns: None
    """
    # Pre-declare variables:

    words: list[str] # list of stored words
    choice: str      # user menu choice
    new_word: str    # average word length


    words: list[str] = [] 
    choice: str = ""
    new_word: str = ""

    print("Words!")

    while choice != "4":
        print("1. Add a word")        
        print("2. Display entries")
        print("3. Display average word length")  
        print("4. Quit")

        choice = input("Action: ")


# Match based on choice

        match choice:
           
            case "1":
                new_word = input("Enter new word: ")
                add_word(words, new_word)

            case "2":
                display_entries(words)

            case "3":
                avg = average_len(words)
                print(f"Average word length: {avg:.2f}")

            case "4":
                print("Thank You!")
            

if __name__ == "__main__":
    main()



