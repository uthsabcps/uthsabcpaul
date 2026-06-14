"""
Task Name: Car Registration

The program demonstrates the use of:
- Enumerated data types (Enum)
- Data classes
- user input with validation.
"""


__author__ = " UTHSAB CHANDRA PAUL SAJIB" 

# Import libraries
from enum import Enum
from dataclasses import dataclass


class CarType(Enum):
    """
    Enumerated number representing different types of cars.
    """

    ICE = "Internal Combustion Engine"
    HEV = "Hybrid Electric Vehicle"
    PHEV = "Plug-in Hybrid Electric Vehicle"
    BEV = "Battery Electric Vehicle"
   

# --- Data Class ---

@dataclass
class Car:
    """
    Stores registration details for a car.
    """

    registration: str # the rego number of a car
    range: int # in KM
    doors: int # total number of doors
    type: CarType # type of car


    def __str__(self) -> str:
        """
        Creates and returns a formatted string describing the car.

        Args: None
        Returns: 
            str: A formatted string representing the car's details.
        """
        
        buffer: str # Stores the range classification
        buffer = ""

        if (self.range < 450):
            buffer = " (Range Class A)"
        elif (self.range >= 600):
            buffer = " (Range Class B)"

        return f"{self.registration}: {self.doors}-door {self.type.name} with a range of {self.range} KM {buffer} "
   
    
def input_car_type() -> CarType:
    """
    Displays a menu and allows the user to select a car type.
    
    Args: None
    Returns:
          A CarType value selected by the user.
    """

    choice: int # Stores the user's menu selection
    result: CarType | None # Selected car type or None initially

    choice = 0
    result = None


    while result is None:
        print("Select car type:")
        print("1. ICE")
        print("2. HEV")
        print("3. PHEV")
        print("4. BEV")

        choice = int(input("Enter choice (1 - 4): "))

        match choice:

             case 1:
               result = CarType.ICE
        
             case 2:
               result = CarType.HEV
            
             case 3:
               result = CarType.PHEV

             case 4:
               result = CarType.BEV

             case _:
               print("Invalid choice. Please try again.")

    return result


def input_car() -> Car:
    """
    Reads user input and creates a Car object.

    Args: None
    Returns:
           A newly created Car object.
    """

    # Registration:

    registration = input("Enter registration: ")
  
    # Range:
  
    range = int(input("Enter range in KM: "))

    # Doors validation:

    doors = 0

    while doors < 2:
       
       doors = int(input("Enter number of doors (minimum 2): "))

       if doors < 2:
           print("Error: A car must have at least 2 doors.")

    # Car type:

    type = input_car_type()

    return Car(registration, range, doors, type)


def main():
    """
    Main entry point of the program.
    """
    car: Car

    print("Enter car registration details")

    car = input_car()

    print("You entered: ")
    print(car)


if __name__ == "__main__":
    main()



        







        


