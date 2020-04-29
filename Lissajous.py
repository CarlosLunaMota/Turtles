from math import sin, cos, pi, ceil
import turtle
import os

"""Drawing Lissajous Curves with Python's Turtle"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200429"


### GLOBAL PARAMETERS ##########################################################

SAVE_IMAGES = True

### LISSAJOUS CUVES ############################################################

def Lissajous(a=3, b=5, delta=pi/2, base_length=100, origin=(0,0), step=0.005):

    half_length = base_length / 2.0

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    x = origin[0] 
    y = origin[1] + half_length*sin(delta)
    turtle.goto((x,y))
    turtle.pendown()

    # Draw the curves:
    for t in range(1, int(ceil(2*pi/step))+1):
        x = origin[0] + half_length*sin(a*t*step)
        y = origin[1] + half_length*sin(b*t*step + delta)
        turtle.goto((x,y))
        
### COMPOSITIONS ###############################################################

def composition_1(X=9, Y=5, base_length=80):

    name = "Lissajous Curves 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    origin = (- X*0.75*base_length, Y*0.75*base_length)
    delta = pi/2

    for x in range(X):
        for y in range(Y):
            o = (origin[0] + 1.5*base_length*x, origin[1] - 1.5*base_length*y)
            Lissajous(x+1, y+1, delta, base_length, o)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Lissajous/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def composition_2(X=9, Y=5, base_length=80):

    name = "Lissajous Curves 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    origin = (- X*0.75*base_length, Y*0.75*base_length)
    

    for x in range(X):
        for y in range(Y):
            o = (origin[0] + 1.5*base_length*x, origin[1] - 1.5*base_length*y)
            delta = pi*x/(X-1)
            Lissajous(1, y+1, delta, base_length, o)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Lissajous/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### MAIN FUNCTION ##############################################################

if __name__ == "__main__":

    #composition_1()
    composition_2()

################################################################################
