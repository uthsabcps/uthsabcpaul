"""
3.3PP Functions: calculate_distance
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"

import math

#Define your new function here

def calculate_distance(velocity: float, time: float) -> float:

    """
    Calculates and returns the stopping distance of a vehicle
    based on its initial velocity and driver's reaction time.
   
    """
    
    FRICTION = 0.7
    GRAVITY = 9.81

    distance = velocity * time + (velocity ** 2) / (2 * FRICTION * GRAVITY)
    return distance


def main():
    # TODO Implement this to call your new function multiple times

    print("Distance Required to Stop")
    
    # Fixed Calculations

    d1 = calculate_distance(22.22 , 1.75)
    print(f"Distance to stop 1: {d1} m")

    d2 = calculate_distance(8.33 , 3.1)
    print(f"Distance to stop 2: {d2} m")
    
    # User input

    velocity: float = float(input("Input initial velocity (m/s) :"))
    time: float = float(input("Input reaction time (seconds): "))

    print("Calculating...")
    
    d3 = calculate_distance(velocity , time)
    print(f"Distance to stop: {d3} m")
    

if __name__ == "__main__":
    main()