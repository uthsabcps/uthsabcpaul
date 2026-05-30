"""
4.3CR User Input Functions
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


#TODO Define input_int here

def input_int(prompt: str, lower: int, upper: int) -> int:
    """
    Prompts the user to enter an integer within a specified 
    valid range. Repeats until the user enters a valid integer that lies 
    between the given lower and upper bounds.

    Args:
        prompt: str # The message to prompt the user with 
        lower: int # The lower bound of the allowed range
        upper: int # the upper bound of the allowed  range

    Returns:
           int: The valid value entered by the user
    """
    
    # Pre-declare variable
    value: int # Value entered by user

    value = int(input(f"{prompt} ({lower} - {upper}): "))

    while value < lower or value > upper:
        print("Value out of range")
        value = int(input(f"{prompt} ({lower} - {upper}): "))

    return value

#TODO Define input_float here

def input_float(prompt: str, lower: float, upper: float) -> float:
    """
    Prompts the user to enter an float within a specified valid range.
    Repeats until the user enters a valid float that lies between the 
    given lower and upper bounds.

    Args:
        prompt: str # The message to prompt the user with
        lower: float # The lower bound of the allowed range
        upper: float # The upper bound of the allowed range

    Returns:
           float: The valid value entered by the user  
    """
   
    # Pre-declare variable
    value: float # Value entered by user

    value = float(input(f"{prompt} ({lower} - {upper}): "))

    while value < lower or value > upper:
        print("Value out of range")
        value = float(input(f"{prompt} ({lower} - {upper}): "))

    return value


#TODO Define input_bool here
def input_bool(prompt: str) -> bool:
    """
    Prompts the user to enter a boolean value using common text forms.
    Accepts 'y', 'yes' or 'true' as True and 'n', 'no' or 'false' as False (case-insensitive)
    Repeats until a valid value is entered

    Args:
        prompt: str # The message to prompt the user with

    Returns:
           bool: The valid value entered by the user
    """
    
    # Pre-declare variable
    user_input: str # Value entered by user

    while True:
        user_input = input(f"{prompt} (yes/no): ").lower()

        if user_input in ['y', 'yes', 'true']:
            return True
    
        elif user_input in ['n', 'no', 'false']:
            return False
    
        else:
            print("Invalid input.\nPlease try again!")


if __name__ == "__main__":
    #All variables are initialised so code will run without error before all functions are implemented and called
    stars = -1     #user's star (between 0 and 5)
    volume = -1.0  #continuously variable speaker volume (as a value between 0 and 11)
    again = False  #do they want to try some action again?

    print("Testing input_int... the number should be saved in stars.")
    print(" - Enter '6' (should loop with error)")
    print(" - Enter '-1' (should loop with error")
    print(" - Enter '2' and it should work")
    stars = input_int("Rate the last movie you saw", 0, 5)
    print(f"Star rating: {stars}");
    print()

    print("Testing input_float... the number should be saved in volume.")
    print(" - Enter '20' (should loop with error)")
    print(" - Enter '-1' (should loop with error)")
    print(" - Enter '9.5' and it should work")
    volume = input_float("Enter amplifier volume", 0.0, 11.0)
    print(f"Volume: {volume}")
    print()

    print("Testing input_bool... the result is saved in again.")
    print(" - Extend these boolean tests by adding more messages to verify your solution!")
    print(" - Enter 'nah' and it should loop with error")
    print(" - Enter 'yes' and it should succeed")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()
    print(" - Verify that it can also read in False...")
    again = input_bool("Try again?")
    print(f"Again: {again}")
    print()

    print("Tests complete...")
