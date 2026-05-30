"""
3.2PP Fill in the Blanks: Tour de France Wrap-up
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


def main():

    """
    Collects user input about the top two riders and displays the final
    Tour de France results.
    """

    print("Tour de France 2025 – Final Standings")
    print()

    first_place: str = input("Enter the name of the rider in first place: ")
    country_1: str = input("What country is the first-placed rider from? ") 
    second_place: str = input("Enter the name of the rider in second place: ")
    country_2: str = input("What country is the second-placed rider from? ") 
    time_1: float = float(input("Enter the total time (in hours) of the first-placed rider: "))
    time_2: float = float(input("Enter the total time (in hours) of the second-placed rider: "))

    margin: float = time_2 - time_1
    
    print(f"{first_place} of {country_1} has claimed victory in the 2025 Tour de France!")
    print(f"They beat {second_place} of {country_2} by just {margin:.2f} hours.")
    print(f"With a total time of {time_1} hours, {first_place} has made history!")


if __name__ == "__main__":
    main()