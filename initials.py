"""
KIT101 2.1PP Turtle Graphics

Turtle Graphics task to draw the author's initials.
Some of the code below has been _over_ commented to help
you understand what is happening.
"""

__author__ = "UTHSAB CHANDRA PAUL SAJIB"

import turtle as painter


def main():
    # Change turtle speed if desired
    # (1=slowest .. 10=fastest | 0=no animation)
    painter.speed(3)

    # Draw your initials below, remembering to use painter.penup() to
    # move without drawing a line...

    # Move left a bit so both letters fit

    painter.penup()
    painter.left(180)
    painter.forward(200) 
    painter.right(180)

    # ---------- Draw U ----------

    painter.pendown()
    painter.pencolor("red")
    painter.right (90)
    painter.forward (200)           # left vertical down
    painter.left (90)
    painter.forward (150)           # bottom horizontal
    painter.left (90)
    painter.forward (200)           # right vertical up

    # Move to start of S 

    painter.penup()
    painter.right(90)
    painter.forward(200)    
    painter.left(90)

    # ---------- Draw S ----------

    painter.pendown()
    painter.pencolor("green")
    painter.left(90)
    painter.forward (100)   # top part         
    painter.left (90)
    painter.forward (100)             # side part down
    painter.left(90)
    painter.forward (100) # middle part 
    painter.right(90)
    painter.forward (100) # lower part
    painter.right(90)
    painter.forward(100) # bottom part

    # Avoid closing the window automatically
    painter.mainloop()


if __name__ == "__main__":
    main()
