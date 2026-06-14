"""
Project 1: Dice Rolling Simulator
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def main():
    """
    The function runs the entire program. 
    """

    import random
    dice_rolling = True

    while dice_rolling:
        print(random.randint(1,6))

        userinput = input("Do you want to roll again? [Yes / No]")

        if userinput == "Yes":
            continue

        else:
            print("The game is over!")
            
            break


if __name__ == "__main__":
     main()
