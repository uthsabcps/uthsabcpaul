
"""
7.1PP Lists of Objects

Task Name: Car Registration

The program demonstrates the use of:
- Enumerated data types (Enum)
- Data classes
- Lists of custom objects
- Functions operating on lists
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

    registration: str # The rego number of a car
    range: int # in KM
    doors: int # Total number of doors
    type: CarType # Type of car


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


def add_car(cars: list[Car]):
   """
   Adds Car object to the list.

   Args:
       cars: list[Car]  # The list that stores Car objects

   Returns: None
   """
   car: Car  # Temporary variable to store new car 
   car = input_car()
   cars.append(car)


def add_many(cars: list[Car], count: int):
   """
   Adds multiple Car objects to the list.

   Args:
       cars: list[Car]  # The list that stores Car objects
       count: int       # Number of cars to add
   
   Returns: None 
   """
   i: int  # Loop counter

   for i in range(count):
      print(f"\nEntering car {i + 1}")
      add_car(cars)


def display_all(cars: list[Car]):
   """
   Displays all the objects, one object per line.

   Args: 
       cars: list[Car]    # The list of Car objects 

   Returns: None
   """
   car: Car  # Stores the current Car in the loop 

   print("\nRegistered Cars:")
   for car in cars:
      print(car)


def best_range(cars: list[Car], type: CarType) -> Car | None:
   """
   Finds the car of a particular type with the longest range.

   Args:
       cars: list[Car]    # List of Car objects
       type: CarType      # The type of cars to search within

   Returns: 
        Car | None  # The car with the longest range, or None if no car of that type is in the collection
   """

   # Pre-declare Variables:
   best: Car | None # The car with the longest range in its motor category
  
   best = None

   for car in cars:
      if car.type == type:
         if best is None or car.range > best.range:
            best = car

   return best 


def average_range(cars: list[Car], type: CarType) -> float:
   """
   Calculate the average range of cars of a particular type.

   Args:
       cars: list[Car]   # The list of Car objects
       type: CarType     # Type of car

   Returns:
          float: Average range of the specified car type
   """
   total: int # Total range of matching cars
   count: int # Number of matching cars

   total = 0
   count = 0

   for car in cars:
      if car.type == type:
         total += car.range
         count += 1

   if count == 0:
      return 0.0
   
   return total / count
      

def main():
    """
    Main entry point of the program.
    """
   
    # Pre-declare variables:

    cars: list[Car] # List of all registered cars 
    initial_count: int # Number of cars added at program start
    choice: int # Menu selection

    cars =[]
    choice = 0

    print("Car Manager")

    initial_count = int(input("Enter initial number of cars:"))
    add_many(cars, initial_count)

    while choice != 5:
       print("\nMenu:")
       print("1. Add another car")
       print("2. Display all cars")
       print("3. Display best range car by type")
       print("4. Display average range by type")
       print("5. Quit")

       choice = int(input("Enter Option:"))

       match choice:
          
           case 1:
               add_car(cars)

           case 2:
               display_all(cars)

           case 3:
               car_type = input_car_type()
               result = best_range(cars, car_type)

               if result is None:               
                   print("No cars of that type.")
               else:
                   print("Best range car:")
                   print(result)

           case 4:
               car_type = input_car_type()
               avg = average_range(cars, car_type)
               print(f"Average range: {avg:.2f} KM")

           case 5:
               print("Thank you!")

           case _:
               print("Invalid Option.")


if __name__ == "__main__":
    main()
    





        







        

