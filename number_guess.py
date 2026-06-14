"""
Project 2: Number Guessing Game
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def main():
    """
    The function runs entire program
    """

    import random

    random_number = random.randrange(0,100)
    user_input = int(input("Guess the number:"))
    
    if user_input > 99:
        print("The number is out of range!"
        "Try Again!")

    elif user_input > random_number:
        print(random_number)
        print("Ops! The number is too big!\nPlease try again!")

    elif user_input < random_number:
        print(random_number)
        print("Ops! The number is too small! \nPlease try again!")

    else:
        print(random_number)
        print("🎉🎉🎉")
        print("Yahoo! The number is correct!")


if __name__ == "__main__":
    main()




     
