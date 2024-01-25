# Your name: Rayan Mostofa
# Your student id: 4970 7916
# Your email: mostofar@umich.edu
# List who or what you worked with on this homework: Just me 
# If you used generative AI also include how you used it.

# import the turtle functions for use in this program
from turtle import *

### write all new functions here ###

def draw_circle(turtle, xpos, ypos, color):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(175, 360)
    turtle.end_fill()
    
    

def draw_rectangle(turtle, xpos, ypos, color):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    
    turtle.end_fill()

def draw_flake(turtle, posx, posy, edges, color):
    
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(posx,posy)
    
    turtle.pendown()
    turtle.pencolor(color)
    for i in range(edges):
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(360/edges)


def draw_sglobe(turtle):
    """
    Write a function to draw a snow globe.  See the instructions for 
    more detail and how you will be graded.

    You can earn extra credit for including block initials in your drawing.
    See the instructions for more details.
    """
    
    draw_circle(turtle, 0, -75, "blue")
    draw_rectangle(turtle, -150, -150, "gray")
    
    black = "black"
    white = "white"
    
    draw_flake(turtle, 100, 72, 7, white)
    draw_flake(turtle, 0, 73, 8, black)
    draw_flake(turtle, -120, 77, 7, white)
    draw_flake(turtle, 110, 150, 9, black)
    draw_flake(turtle, 5, 150, 6, black)
    draw_flake(turtle, -115, 150, 9, white)
    draw_flake(turtle, -7, 200, 8, black)
    draw_flake(turtle, 102, 200, 6, black)
    draw_flake(turtle, 120, 18, 7, white)
    draw_flake(turtle, 19,  10, 8, black)
    draw_flake(turtle, -75, 25, 7, black)
    


def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_sglobe.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """
    
    space = Screen()
    t = Turtle()
    
    space.screensize(400,450)
    space.bgcolor("pink")
    
    draw_sglobe(t)
    
    space.exitonclick()
     


# # Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
