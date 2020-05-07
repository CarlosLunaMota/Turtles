from math import pi, sin, cos, sqrt
import turtle
import os

"""Drawing Vogel Models with Python's Turtle"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200507"


### GLOBAL PARAMETERS ##########################################################

SAVE_IMAGES = True

### VOGEL MODEL ################################################################

def Vogel(angle=2.0*pi/((1.0+sqrt(5.0))/2.0), k=2.0, color="goldenrod", origin=(0,0), points=5000):

    name = "Vogel Model"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)
    turtle.penup()
    turtle.color(color)

    # Draw first point:
    turtle.goto((origin[0]+k, origin[1]))
    turtle.dot()

    # Draw the rest of the points:
    for i in range(1,points):
        a = angle*i
        r = k*sqrt(a)
        turtle.goto((origin[0] + r*cos(a), origin[1] + r*sin(a)))
        turtle.dot()

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Vogel/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### MAIN FUNCTION ##############################################################

if __name__ == "__main__": Vogel()

################################################################################
