from math import pi, sin, cos
import turtle
import random
import os

"""Drawing Chaotic Fractals with Python's Turtle"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200507"


### GLOBAL PARAMETERS ##########################################################

SAVE_IMAGES = True

### CHAOS FRACTALS #############################################################

def Chaos_1(sides=3, k=0.5, color="darkblue", origin=(0,0), r=200, points=2000, restricted=False):

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)
    turtle.penup()
    turtle.color(color)

    # Generate Polygon:
    a = 2.0*pi/sides
    P = [(origin[0] - r*sin(a*i), origin[1] + r*cos(a*i)) for i in range(sides)]

    # Draw the polygon vertices:
    for point in P:
        turtle.goto(point)
        turtle.dot()

    # Draw the rest of the fractal:
    vertex = P[0]
    point  = P[0]
    for i in range(points*sides):
        if restricted: vertex = random.choice([v for v in P if v != vertex])
        else:          vertex = random.choice(P)
        point  = (k*vertex[0]+(1.0-k)*point[0], k*vertex[1]+(1.0-k)*point[1])
        turtle.goto(point)
        turtle.dot(2,)
        
def Chaos_2(sides=3, k=0.5, color="darkblue", origin=(0,0), r=200, points=2000, restricted=False):

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)
    turtle.penup()
    turtle.color(color)

    # Generate Polygon:
    a = 2.0*pi/sides
    P = [(origin[0] - r*sin(a*i), origin[1] + r*cos(a*i)) for i in range(sides)]
    for i in range(sides):
        P.append(((P[i-1][0]+P[i][0])/2.0, (P[i-1][1]+P[i][1])/2.0))

    # Draw the polygon vertices:
    for point in P:
        turtle.goto(point)
        turtle.dot()

    # Draw the rest of the fractal:
    vertex = P[0]
    point  = P[0]
    for i in range(points*sides):
        if restricted: vertex = random.choice([v for v in P if v != vertex])
        else:          vertex = random.choice(P)
        point  = (k*vertex[0]+(1.0-k)*point[0], k*vertex[1]+(1.0-k)*point[1])
        turtle.goto(point)
        turtle.dot(2,)
            
### COMPOSITIONS ###############################################################

def Composition_1():

    name = "Chaotic Fractals"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Draw the fractals:
    Chaos_1(sides=3, k=0.5,     color="green", origin=(-450,0))
    Chaos_2(sides=4, k=2/3.0,   color="red",   origin=(   0,0))
    Chaos_1(sides=5, k=1/1.618, color="blue",  origin=( 450,0))

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Chaos/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### MAIN FUNCTION ##############################################################

if __name__ == "__main__":

    Composition_1()

################################################################################
