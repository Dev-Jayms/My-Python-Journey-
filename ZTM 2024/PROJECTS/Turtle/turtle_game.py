"""This code import the turtle module"""
import turtle
"""
This code draw a dash line with the turtle
"""


# Create a turtle object
tim = turtle.Turtle()

# Set the dash length and gap length
dash_length = 10
gap_length = 10

# Draw a dashed line
for _ in range(15):  # Adjust the range for the length of the line
    tim.forward(dash_length)  # Draw a dash
    tim.penup()  # Lift the pen to create a gap
    tim.forward(gap_length)  # Move forward without drawing
    tim.pendown()  # Lower the pen to draw again

# Keep the window open until closed by the user
turtle.done()
