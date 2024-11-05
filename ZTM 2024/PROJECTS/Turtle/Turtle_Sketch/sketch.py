from turtle import Turtle, Screen
# Import the necessary modules from the turtle library
from turtle import Turtle, Screen

# Create a new turtle object named snake
tim = Turtle()

# Create a new screen object
screen = Screen()


def move_forward():
    """
    Move the turtle forward by 10 units.

    This function is bound to the 'w' key.
    """
    # Move the turtle forward by 10 units
    tim.forward(10)

def move_backward():
    """
    Move the turtle backward by 10 units.

    This function is bound to the 's' key.
    """
    # Move the turtle backward by 10 units
    tim.backward(10)

def turn_left():
    """
    Turn the turtle left by 10 degrees.

    This function is bound to the 'a' key.
    """
    # Get the current heading of the turtle
    # Add 10 degrees to the current heading
    new_heading = tim.heading() + 10
    # Set the new heading
    tim.setheading(new_heading)

def turn_right():
    """
    Turn the turtle right by 10 degrees.

    This function is bound to the 'd' key.
    """
    # Get the current heading of the turtle
    # Subtract 10 degrees from the current heading
    new_heading = tim.heading() - 10
    # Set the new heading
    tim.setheading(new_heading)

def clear():
    """
    Clear the turtle's drawing and reset its position.

    This function is bound to the 'c' key.
    """
    # Clear the turtle's drawing
    tim.clear()
    # Lift the pen to move the turtle without drawing
    tim.penup()
    # Move the turtle to the origin (0, 0)
    tim.home()
    # Lower the pen to start drawing again
    tim.pendown()

# Start listening for keyboard events
screen.listen()

# Bind the movement functions to their respective keys
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# Exit the program when the user clicks on the screen
screen.exitonclick()
