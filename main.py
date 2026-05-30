"""
Main Heading Main Program

Handles user interaction and menu heading processing
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


# Import module
import operations


def main():
    """
    Runs the MD Heading application 
    """
    # Pre-declare Variables:
    text: str  # Stores user input heading
    words: list[str]  # Stores heading as list of words
    level: int  # Stores current heading level (1-6)
    choice: str  # Stores user menu choice
    new_level: int  # Stores new heading level input
    is_running: bool  # Controls loop 

    print("Md Heading")
    print()

    text = input("Enter heading: ")
    words = text.split()

    level = 1
    is_running = True

    while is_running:
        print()
        print(operations.get_markdown(words, level))

        print("\nMenu:")
        print("1. Change level")
        print("2. Title Case")
        print("3. Show ID")
        print("4. Show HTML")
        print("5. Quit")

        choice = input("Choose: ")

        match choice:

            case "1":
                new_level = int(input("Enter level (1-6): "))

                while new_level < 1 or new_level > 6:
                    new_level = int(input("Invalid! Enter 1-6: "))

                level = new_level

            case "2":
                operations.make_title_case(words)

            case "3":
                print(operations.get_id(words, level))

            case "4":
                print(operations.get_html(words, level))

            case "5":
                is_running = False


if __name__ == "__main__":
    main()







