import turtle
import os

"""Drawing Fractal Curves with Python's Turtle"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200428"


### GLOBAL PARAMETERS ##########################################################

SAVE_IMAGES = True

### DRAGON CUVES ###############################################################

def Dragon_1(order=12, base_length=4, origin=(-250,100)):

    name = "Dragon Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*(order+2))
    turtle.pendown()

    # Draw the curve:
    turtle.color("darkgreen")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.circle(-base_length, 90, 32)
        else:                     turtle.circle( base_length, 90, 32)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_2(order=14, base_length=5, origin=(-300,150)):

    name = "Dragon Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*order)
    turtle.pendown()

    # Draw the curve:
    colors = ("darkgreen", "yellowgreen")
    for step in range(1,order+1):
        turtle.color(colors[step % len(colors)])
        for i in range(1<<(step-1), 1<<step):
            if (((i & -i) << 1) & i): turtle.right(90)
            else:                     turtle.left(90)
            turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_twins_1(order=14, base_length=4, origin=(-300,25)):

    name = "Dragon Curve - Twins 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(135*(order+2))
    turtle.pendown()

    # Draw the first curve:
    turtle.color("yellowgreen")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.color("darkgreen")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_twins_2(order=14, base_length=4, origin=(-400,150)):

    name = "Dragon Curve - Twins 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*(order+2))
    turtle.pendown()

    # Draw the first half of the the first curve:
    turtle.color("darkgreen")
    for i in range(1<<(order-1)):
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)
        turtle.forward(base_length)

    # Remember the middle point:
    p = turtle.position()

    # Draw the second half of the the first curve:
    for i in range(1<<(order-1), 1<<order):
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)
        turtle.forward(base_length)

    # Return to the middle point:
    turtle.penup()
    turtle.goto(p)
    turtle.pendown()

    # Draw the second curve:
    turtle.color("yellowgreen")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_twins_3(order=13, base_length=4, origin=(0,200)):

    name = "Dragon Curve - Twins 3"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*(order+3))
    turtle.pendown()

    # Draw the first half of the the first curve:
    turtle.color("darkgreen")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)
        turtle.forward(base_length)

    # Move to the new origin:
    p = turtle.position()
    dist = ((origin[0]-p[0])**2 + (origin[1]-p[1])**2)**0.5
    turtle.penup()
    turtle.goto(origin)
    turtle.left(45*(order+2))
    turtle.forward(dist//2)
    turtle.left(90)
    turtle.forward(dist)
    turtle.right(45*(order-4))
    turtle.pendown()

    # Draw the second curve:
    turtle.color("yellowgreen")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_quadruplets_1(order=12, base_length=4, origin=(-50,25)):

    name = "Dragon Curve - Quadruplets 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)

    # Basic Dragon setup:
    Dragon = turtle.Turtle()
    Dragon.hideturtle()
    Dragon.speed(0)
    Dragon.penup()
    Dragon.goto(origin)
    Dragon.pendown()

    # Define the four dragons:
    Dragon_1 = Dragon.clone()
    Dragon_1.color("red")
    Dragon_1.left(0 + 45*order)

    Dragon_2 = Dragon.clone()
    Dragon_2.color("darkgreen")
    Dragon_2.left(90 + 45*order)

    Dragon_3 = Dragon.clone()
    Dragon_3.color("gold")
    Dragon_3.left(180 + 45*order)

    Dragon_4 = Dragon.clone()
    Dragon_4.color("darkblue")
    Dragon_4.left(270 + 45*order)

    # Draw the four curves at the same time:
    for i in reversed(range(1<<order)):

        Dragon_1.forward(base_length)
        Dragon_2.forward(base_length)
        Dragon_3.forward(base_length)
        Dragon_4.forward(base_length)

        if (((i & -i) << 1) & i):
            Dragon_1.right(90)
            Dragon_2.right(90)
            Dragon_3.right(90)
            Dragon_4.right(90)
        else:
            Dragon_1.left(90)
            Dragon_2.left(90)
            Dragon_3.left(90)
            Dragon_4.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_quadruplets_2(order=12, base_length=4, origin=(-50,25)):

    name = "Dragon Curve - Quadruplets 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)

    # Basic Dragon setup:
    Dragon = turtle.Turtle()
    Dragon.hideturtle()
    Dragon.speed(0)
    Dragon.penup()
    Dragon.goto(origin)
    Dragon.pendown()

    # Define the four dragons:
    Dragon_1 = Dragon.clone()
    Dragon_1.color("red")
    Dragon_1.left(0 + 45*order)

    Dragon_2 = Dragon.clone()
    Dragon_2.color("darkgreen")
    Dragon_2.left(90 + 45*order)

    Dragon_3 = Dragon.clone()
    Dragon_3.color("gold")
    Dragon_3.left(180 + 45*order)

    Dragon_4 = Dragon.clone()
    Dragon_4.color("darkblue")
    Dragon_4.left(270 + 45*order)

    # Draw the four curves at the same time:
    for i in range(1<<order):

        if (((i & -i) << 1) & i):
            Dragon_1.left(90)
            Dragon_2.left(90)
            Dragon_3.left(90)
            Dragon_4.left(90)
        else:
            Dragon_1.right(90)
            Dragon_2.right(90)
            Dragon_3.right(90)
            Dragon_4.right(90)

        Dragon_1.forward(base_length)
        Dragon_2.forward(base_length)
        Dragon_3.forward(base_length)
        Dragon_4.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_quadruplets_3(order=12, base_length=5, origin=(100,200)):

    name = "Dragon Curve - Quadruplets 3"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(135*order)
    turtle.pendown()

    # Draw first curve:
    turtle.color("darkblue")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw second curve:
    turtle.color("gold")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    turtle.right(90)

    # Draw third curve:
    turtle.color("darkgreen")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw fourth curve:
    turtle.color("red")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Dragon_quadruplets_4(order=12, base_length=5, origin=(-300,-100)):

    name = "Dragon Curve - Quadruplets 4"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(180 + 135*order)
    turtle.pendown()

    # Draw first curve:
    turtle.color("red")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw second curve:
    turtle.color("darkblue")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    turtle.right(90)

    # Draw third curve:
    turtle.color("gold")
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.left(90)

    # Draw fourth curve:
    turtle.color("darkgreen")
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### TERDRAGON CURVES ###########################################################

def Terdragon_1(order=8, base_length=3, origin=(-400,50)):

    name = "Terdragon Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Draw the curve:
    turtle.color("darkblue")
    for i in range(1, 3**order + 1):
        turn = i
        while turn % 3 == 0: turn //= 3
        if turn % 3 == 1:
            turtle.left(60)
            turtle.forward(base_length)
            turtle.left(60)
            turtle.forward(base_length)
        else:
            turtle.right(60)
            turtle.forward(base_length)
            turtle.right(60)
            turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Terdragon_2(order=8, base_length=3, origin=(-400,50)):

    name = "Terdragon Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Draw the first curve:
    turtle.color("cornflowerblue")
    for i in range(3**(order-1)):
        turn = i+1
        while turn % 3 == 0: turn //= 3
        if turn % 3 == 1:
            turtle.left(60)
            turtle.forward(base_length)
            turtle.left(60)
            turtle.forward(base_length)
        else:
            turtle.right(60)
            turtle.forward(base_length)
            turtle.right(60)
            turtle.forward(base_length)

    # Draw the second curve:
    turtle.color("darkblue")
    for i in range(3**(order-1), 2*(3**(order-1))):
        turn = i+1
        while turn % 3 == 0: turn //= 3
        if turn % 3 == 1:
            turtle.left(60)
            turtle.forward(base_length)
            turtle.left(60)
            turtle.forward(base_length)
        else:
            turtle.right(60)
            turtle.forward(base_length)
            turtle.right(60)
            turtle.forward(base_length)

    # Draw the third curve:
    turtle.color("cornflowerblue")
    for i in range(2*(3**(order-1)), 3**order):
        turn = i+1
        while turn % 3 == 0: turn //= 3
        if turn % 3 == 1:
            turtle.left(60)
            turtle.forward(base_length)
            turtle.left(60)
            turtle.forward(base_length)
        else:
            turtle.right(60)
            turtle.forward(base_length)
            turtle.right(60)
            turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### GOSPER CURVES ##############################################################

def Gosper_1(order=5, base_length=4, origin=(-100,-250)):

    name = "Gosper Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Build instructions sequence:
    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "A-B--B+A++AA+B-"
            elif char == "B": new_seq += "+A-BB--B-A++A+B"
            else:             new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("firebrick")
    for char in seq:
        if   char == "-": turtle.right(60)
        elif char == "+": turtle.left(60)
        else:             turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Gosper_2(order=5, base_length=4, origin=(-100,-250)):

    name = "Gosper Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Build instructions sequence:
    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "A-B--B+A++AA+B-"
            elif char == "B": new_seq += "+A-BB--B-A++A+B"
            else:             new_seq += char
        seq = new_seq

    # Draw the curve:
    N = len(seq)//7
    colors = ("firebrick", "darkorange", "red", "darkorange",
              "firebrick", "darkorange", "firebrick")
    for i in range(7):
        turtle.color(colors[i])
        for char in seq[i*N: (i+1)*N]:
            if   char == "-": turtle.right(60)
            elif char == "+": turtle.left(60)
            else:             turtle.forward(base_length)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### FIBONACCI WORD #############################################################

def Fibonacci_1(order=18, base_length=3, origin=(-400,-200)):

    name = "Fibonacci Word Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    S, SS  = "0", "01"
    for i in range(order): S, SS = SS, SS+S

    # Draw the curve:
    turtle.color("purple")
    for i, char in enumerate(S):
        turtle.forward(base_length)
        if char == "0":
            if i%2: turtle.right(90)
            else:   turtle.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Fibonacci_2(order=18, base_length=3, origin=(-400,-200)):

    name = "Fibonacci Word Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    F, S, SS = [0,1], "0", "01"
    for i in range(order):
        F.append(len(SS))
        S, SS = SS, SS+S

    # Draw the curve:
    colors = ("purple", "deeppink", "magenta")
    for i in range(1,len(F)):
        turtle.color(colors[i%3])
        for j in range(F[i-1], F[i]):
            turtle.forward(base_length)
            if S[j] == "0":
                if j%2: turtle.right(90)
                else:   turtle.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### HILBERT ####################################################################

def Hilbert_1(order=7, base_length=5, origin=(-350,-300)):

    name = "Hilbert Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    seq = "a"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "a": new_seq += "-bF+aFa+Fb-"
            elif char == "b": new_seq += "+aF-bFb-Fa+"
            else:             new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("dodgerblue")
    for char in seq:
        if   char == "F": turtle.forward(base_length)
        elif char == "+": turtle.right(90)
        elif char == "-": turtle.left(90)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Hilbert_2(order=7, base_length=5, origin=(-350,-300)):

    name = "Hilbert Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    seq = "a"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "a": new_seq += "-bF+aFa+Fb-"
            elif char == "b": new_seq += "+aF-bFb-Fa+"
            else:             new_seq += char
        seq = new_seq
    seq = seq.replace("a", "")
    seq = seq.replace("b", "")

    # Draw the curve:
    color,i,j = "blue",1,4
    turtle.color(color)
    for char in seq:
        if i == j:
            if color == "blue": color = "dodgerblue"
            else:               color = "blue"
            turtle.color(color)
            j *= 4
        if   char == "+": turtle.right(90)
        elif char == "-": turtle.left(90)
        else:
            turtle.forward(base_length)
            i += 1

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### LEBESGUE ###################################################################

def Lebesgue_1(order=6, base_length=10, origin=(-350,350)):

    name = "Lebesgue Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Draw the curve:
    turtle.color("darkred")
    for i in range(1<<(2*order)):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Lebesgue_2(order=6, base_length=10, origin=(-350,350)):

    name = "Lebesgue Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Draw the curve:
    color,j = "red",4
    turtle.color(color)
    for i in range(1<<(2*order)):
        if i == j:
            if color == "red": color = "darkred"
            else:              color = "red"
            turtle.color(color)
            j *= 4
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### KOCH #######################################################################

def Koch_1(order=7, base_length=0.5, origin=(-575,-100)):

    name = "Koch Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    seq = "F"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if char == "F": new_seq += "F+F--F+F"
            else:           new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("darkgoldenrod")
    for char in seq:
        if   char == "F": turtle.forward(base_length)
        elif char == "+": turtle.right(-60)
        elif char == "-": turtle.left(-60)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Koch_2(order=5, base_length=2, origin=(-300,200)):

    name = "Koch Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    # Build instructions sequence:
    seq = "F--F--F"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if char == "F": new_seq += "F+F--F+F"
            else:           new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("darkgoldenrod")
    for char in seq:
        if   char == "F": turtle.forward(base_length)
        elif char == "+": turtle.right(-60)
        elif char == "-": turtle.left(-60)

    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### SIERPINSKI #################################################################

def Sierpinski_1(order=8, base_length=3, origin=(-425,-300)):

    name = "Sierpinski Arrowhead Curve 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    if order % 2: turtle.left(60)
    turtle.pendown()

    # Build instructions sequence:
    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "B-A-B"
            elif char == "B": new_seq += "A+B+A"
            else:             new_seq += char
        seq = new_seq

    # Draw the curve:
    turtle.color("darkgreen")
    for char in seq:
        if   char == "+": turtle.right(-60)
        elif char == "-": turtle.left(-60)
        else:             turtle.forward(base_length)
        
    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Sierpinski_2(order=8, base_length=3, origin=(-425,-300)):

    name = "Sierpinski Arrowhead Curve 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    if order % 2: turtle.left(60)
    turtle.pendown()

    # Build instructions sequence:
    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "B-A-B"
            elif char == "B": new_seq += "A+B+A"
            else:             new_seq += char
        seq = new_seq

    # Draw the curve:
    i,j = 0,9
    color = "darkgreen"
    turtle.color(color)
    for char in seq:
        if   char == "+": turtle.right(-60)
        elif char == "-": turtle.left(-60)
        else:
            turtle.forward(base_length)
            i += 1
            if i == j:
                if color == "darkgreen": color = "yellowgreen"
                else:                    color = "darkgreen"
                turtle.color(color)
                j *= 3
            
    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

def Sierpinski_3(order=8, base_length=3, origin=(-50,-300)):

    name = "Sierpinski Arrowhead Curve 3"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle setup:
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    if order % 2: turtle.left(120)
    else:         turtle.left(180)
    turtle.pendown()

    # Build instructions sequence:
    seq = "B"
    for i in range(order-1):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "B-A-B"
            elif char == "B": new_seq += "A+B+A"
            else:             new_seq += char
        seq = new_seq

    # Draw the first curve:
    turtle.color("darkgreen")
    for char in seq:
        if   char == "+": turtle.right(60)
        elif char == "-": turtle.left(60)
        else:             turtle.forward(base_length)
    
    if order % 2: turtle.right(120)

    # Draw the second curve:
    turtle.color("yellowgreen")
    for char in seq:
        if   char == "+": turtle.right(60)
        elif char == "-": turtle.left(60)
        else:             turtle.forward(base_length)

    if order % 2: turtle.right(120)

    # Draw the third curve:
    turtle.color("springgreen")
    for char in seq:
        if   char == "+": turtle.right(60)
        elif char == "-": turtle.left(60)
        else:             turtle.forward(base_length)
        
    # Save the drawing:
    if SAVE_IMAGES:
        name = "Fractals/"+name
        turtle.getscreen().getcanvas().postscript(file=name+".ps")
        name = name.replace(" ", "\ ")
        conversion  = "gs -dSAFER -dBATCH -dQUIET -dNOPAUSE -sDEVICE=pngalpha"
        conversion += " -dEPSCrop -r600 -sOutputFile="+name+".png "+name+".ps"
        os.system(conversion)

    # Close the window:
    turtle.exitonclick()

### MAIN FUNCTION ##############################################################

if __name__ == "__main__":

    #Dragon_1()
    #Dragon_2()
    #Dragon_twins_1()
    #Dragon_twins_2()
    #Dragon_twins_3()
    #Dragon_quadruplets_1()
    #Dragon_quadruplets_2()
    #Dragon_quadruplets_3()
    #Dragon_quadruplets_4()

    #Terdragon_1()
    #Terdragon_2()

    #Gosper_1()
    #Gosper_2()

    #Fibonacci_1()
    #Fibonacci_2()

    #Hilbert_1()
    #Hilbert_2()

    #Lebesgue_1()
    #Lebesgue_2()

    #Koch_1()
    #Koch_2()

    #Sierpinski_1()
    #Sierpinski_2()
    Sierpinski_3()

################################################################################
