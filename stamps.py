"""
3.4CR Stamp Function

Implements a reusable 'stamp' that can draw the author's initials at
any location on the Turtle Graphics window.
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"


# Import libraries
from turtle import Turtle


def place_stamp(stamper: Turtle, x: float, y: float, ink: str):
    """
    Draws the author's initials with the bottom-left corner positioned.

    Args:
        stamper: Turtle  # The turtle object used for drawing
        x: float  # The x-coordinator of hte bottom-left corner
        y: float  # The y-coordinator of the bottom-left corner
        ink: str  # The colour of the drawing

    Returns: None
    """
    # Pre-declare variables
    old_ink: str #  Previous pen colour
    old_direction: float # Previous angle
    old_x: float # Previous x position
    old_y: float # Previous y position 

    # Save current turtle state
    old_ink = stamper.pencolor()
    old_direction = stamper.heading()
    old_x = stamper.xcor()
    old_y = stamper.ycor()

    # Set the colour to ther value of ink
    stamper.pencolor(ink)

    # Move to the correct drawing position
    stamper.penup()
    stamper.goto(x + 200, y + 200)
    stamper.setheading(0)
    stamper.pendown()

    # ---------- Draw U ----------
    stamper.pendown()
    stamper.right (90)
    stamper.forward (200) # left vertical down
    stamper.left (90)
    stamper.forward (150) # bottom horizontal
    stamper.left (90)
    stamper.forward (200) # right vertical up

    # Move to start of S    
    stamper.penup()
    stamper.right(90)
    stamper.forward(200)    
    stamper.left(90)

    # ---------- Draw S ----------
    stamper.pendown()
    stamper.left(90) # turn left
    stamper.forward (100) # top part            
    stamper.left (90)  
    stamper.forward (100) # side part 
    stamper.left(90)
    stamper.forward (100) # middle part
    stamper.right(90)
    stamper.forward (100) # lower part
    stamper.right(90)
    stamper.forward(100) # bottom part

    # Restore turtle state
    stamper.penup()
    stamper.goto(old_x, old_y)
    stamper.pencolor(old_ink)
    stamper.setheading(old_direction)


def main():
    """
    Runs the Turtle stamp program.

    Args: None
    Returns: None
    """
    # Pre-declare variablres
    t = Turtle() # The turtle graphics object
    t.speed(3)
    
    # Draw stamps at different locations and colours
    place_stamp(t, -500, 150, "red")
    place_stamp(t, 50, -100,  "blue")
    place_stamp(t, -800, -200, "green")
    
    # Aviod closing the window automatically 
    t.screen.mainloop()


if __name__ == "__main__":
    main()
