from math import sqrt
import turtle
import os

"""Drawing Boards for board games"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200507"


### GLOBAL PARAMETERS ##########################################################

SAVE_IMAGES = True

### BASIC SHAPES ###############################################################

def triangle(center, radius, angle, thickness, color):

    # Get a turtle:
    t = turtle.Turtle()
    t.pensize(thickness)
    t.color(color)
    t.hideturtle()
    t.speed(0)
    
    # Draw the triangle:    
    t.penup()
    t.goto(center)
    t.left(angle+90)
    t.forward(radius)
    t.pendown()
    t.left(150)
    for i in range(4):
        t.forward(sqrt(3.0)*radius)
        t.left(120)

def square(center, radius, angle, thickness, color):

    # Get a turtle:
    t = turtle.Turtle()
    t.pensize(thickness)
    t.color(color)
    t.hideturtle()
    t.speed(0)

    # Draw the triangle:    
    t.penup()
    t.goto(center)
    t.left(angle+45)
    t.forward(radius)
    t.pendown()
    t.left(135)
    for i in range(5):
        t.forward(sqrt(2.0)*radius)
        t.left(90)    

def hexagon(center, radius, angle, thickness, color):

    # Get a turtle:
    t = turtle.Turtle()
    t.pensize(thickness)
    t.color(color)
    t.hideturtle()
    t.speed(0)

    # Draw the triangle:    
    t.penup()
    t.goto(center)
    t.left(angle+90)
    t.forward(radius)
    t.pendown()
    t.left(120)
    for i in range(7):
        t.forward(radius)
        t.left(60)

### BOARS ######################################################################

def Rectangle_of_Squares(width=8, height=7, length=85, origin=(-300,-100), thickness=8, color="black"):

    name = "Rectangle of Squares "+str(width)+"x"+str(height)

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)
    turtle.hideturtle()
    turtle.delay(0)

    # Draw the squares:
    angle  = 0
    radius = length/sqrt(2.0)
    delta  = (sqrt(2.0)*radius, sqrt(2.0)*radius)
    for h in range(height):
        for w in range(width):
            center = (origin[0]+delta[0]*w, origin[1]-150+delta[1]*h)
            square(center, radius, angle, thickness, color)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Boards/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Triangle_of_Triangles(side=8, length=85, origin=(-300,-200), thickness=5, color="black"):

    name = "Triangle of Triangles "+str(side)

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)
    turtle.hideturtle()
    turtle.delay(0)

    # Draw the triangles:
    angle  = 0
    radius = length/sqrt(3.0)
    delta  = (sqrt(3.0)*radius, 3.0*radius/2.0)
    for h in range(side):
        for w in range(side-h):
            center = (origin[0]+delta[0]*w+delta[0]*h/2.0, origin[1]+delta[1]*h)
            triangle(center, radius, angle, thickness, color)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Boards/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Triangle_of_Hexagons(side=8, length=85, origin=(-300,-200), thickness=5, color="black"):

    name = "Triangle of Hexagons "+str(side)

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)
    turtle.hideturtle()
    turtle.delay(0)
    

    # Draw the triangles:
    angle  = 0
    radius = length/sqrt(3.0)
    delta  = (sqrt(3.0)*radius, 3.0*radius/2.0)
    for h in range(side):
        for w in range(side-h):
            center = (origin[0]+delta[0]*w+delta[0]*h/2.0, origin[1]+delta[1]*h)
            hexagon(center, radius, angle, thickness, color)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Boards/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Hexagon_of_Hexagons(side=4, length=85, origin=(-300,-200), thickness=5, color="black"):

    name = "Hexagon of Hexagons "+str(side)

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)
    turtle.hideturtle()
    turtle.delay(0)
    
    # Draw the triangles:
    angle  = 0
    radius = length/sqrt(3.0)
    delta  = (sqrt(3.0)*radius, 3.0*radius/2.0)
    for h in range(side):
        for w in range(side+h):
            center = (origin[0]+delta[0]*w-delta[0]*h/2.0, origin[1]+delta[1]*h)
            hexagon(center, radius, angle, thickness, color)
        for w in range(side+h):
            center = (origin[0]+delta[0]*w-delta[0]*h/2.0, origin[1]+delta[1]*(2*side-h-2))
            hexagon(center, radius, angle, thickness, color)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Boards/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### MAIN FUNCTION ##############################################################

if __name__ == "__main__":

    #Rectangle_of_Squares()
    #Triangle_of_Triangles()
    #Triangle_of_Hexagons()
    Hexagon_of_Hexagons()

################################################################################
