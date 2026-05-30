"""
4.1PP Selection and Repetition
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"

import timeit # used for timing the execution of code
from random import randint # used for generating random values


def show_heading(heading: str):
    """
    Displays the given heading in ALL CAPS, underlined by plus (+) symbols
    and followed by a blank line.
    """
    #TODO Complete the implementation of this function (replace the ellipsis ...)

    print(heading.upper())
    print("+" * len(heading))
    print()


def one_attempt(num1: int, num2: int) -> bool:
    """
    Tests the user's ability to answer a given problem, providing feedback on
    the attempt. Returns True if they answer correctly, False otherwise.
    """

    # pre-declare variables:

    attempt: int # the user's typed answer
    correct: bool # indicates whether the answer is correct

    #TODO Complete the implementation of this function

    attempt = int(input(f"What is {num1} - {num2}? "))
    correct = True

    if attempt == num1 - num2:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {num1 - num2}")
        correct = False

    return correct #TODO Update this line


def run_tutorial(max: int, target: int) -> int:
    """
    Tests the user's maths ability by having them answer a series of
    problems correctly until a target number is answered correctly.
    Returns the total number of attempts.
    """

    # Pre-declare variables:
    
    attempts: int # the total number of attempts made by the user
    correct: int # the number of correct answers so far
    a: int # random operand A
    b: int # random operand B

    attempts = 0
    correct = 0

    #TODO Complete the implementation of this function
    
    #one_attempt(10, 5) #TODO Change these dummy parameter values
    
    while correct < target:
        a = randint(1, max)
        b = randint(1, max)

        attempts += 1

        if one_attempt(a, b):
            correct += 1

    return attempts #TODO When implementing this function change this line to return attempts


def main():
    MAX = 20 # maximum operand value of random numbers
    REQUIRED = 5 # required number of correct answers
    start_time: float # start time of tutorial
    end_time: float # end time of tutorial
    attempted: int # number of problems user attempted before solving REQUIRED problems

    show_heading("Maths Tutorial")
    print("You need to correctly solve subtraction problems as quickly as you can.");
    print(f"You need to answer {REQUIRED} problems correctly before the tutorial ends.");
    print(f"The operand values will be between 1 and {MAX}.");
    print();

    #Run the tutorial session
    input("Press Enter to start the timed test")
    start_time = timeit.default_timer()
    attempted = run_tutorial(MAX, REQUIRED)
    end_time = timeit.default_timer()

    #Report on the user's performance
    print()
    print("Attempts:", attempted)
    print(f"Accuracy: {(100 * REQUIRED / attempted):.1f}%")
    print(f"Total time: {(end_time - start_time):3.1f} s")
    print()
    show_heading("Keep practicing to improve your skills!")


if __name__ == "__main__":
    main()
