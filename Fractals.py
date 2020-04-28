import turtle

"""Drawing Fractal Curves with Python's Turtle"""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200428"


### DRAGON CUVES ###############################################################

def Dragon(order=12, base_length=4, origin=(-250,100)):

    name = "Dragon Curve"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.color("yellow")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*(order+2))
    turtle.pendown()

    # Draw the curve:
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.circle(-base_length, 90, 32)
        else:                     turtle.circle( base_length, 90, 32)

    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()

def Dragon_bitone(order=14, base_length=5, origin=(-300,150)):

    name = "Dragon Curve - bitone"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*order)
    turtle.pendown()

    # Draw the curve:
    colors = ("yellow", "green")
    for step in range(1,order+1):
        turtle.color(colors[step % len(colors)])
        for i in range(1<<(step-1), 1<<step):
            if (((i & -i) << 1) & i): turtle.right(90)
            else:                     turtle.left(90)
            turtle.forward(base_length)

    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()
    
def Dragon_twins_1(order=14, base_length=4, origin=(-300,25)):

    name = "Dragon Curve - Twins 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(135*(order+2))
    turtle.pendown()

    # Draw the first curve:
    turtle.color('blue')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.color('yellow')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)


    
    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()

def Dragon_twins_2(order=14, base_length=4, origin=(-400,150)):

    name = "Dragon Curve - Twins 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(45*(order+2))
    turtle.pendown()

    # Draw the first half of the the first curve:
    turtle.color('blue')    
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
    turtle.color('yellow')    
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
    
    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()

def Dragon_quadruplets_1(order=12, base_length=4, origin=(-50,25)):

    name = "Dragon Curve - Quadruplets 1"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.delay(0)

    # Basic Dragon set-up:
    Dragon = turtle.Turtle()
    Dragon.hideturtle()
    Dragon.speed(0)
    Dragon.penup()
    Dragon.goto(origin)
    Dragon.pendown()

    # Define the four dragons:
    Dragon_1 = Dragon.clone()
    Dragon_1.color('blue')
    Dragon_1.left(0 + 45*order)
    
    Dragon_2 = Dragon.clone()
    Dragon_2.color('orange')
    Dragon_2.left(90 + 45*order)
    
    Dragon_3 = Dragon.clone()
    Dragon_3.color('green')
    Dragon_3.left(180 + 45*order)
    
    Dragon_4 = Dragon.clone()
    Dragon_4.color('yellow')
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
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()
    
def Dragon_quadruplets_2(order=12, base_length=4, origin=(-50,25)):

    name = "Dragon Curve - Quadruplets 2"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.delay(0)

    # Basic Dragon set-up:
    Dragon = turtle.Turtle()
    Dragon.hideturtle()
    Dragon.speed(0)
    Dragon.penup()
    Dragon.goto(origin)
    Dragon.pendown()

    # Define the four dragons:
    Dragon_1 = Dragon.clone()
    Dragon_1.color('blue')
    Dragon_1.left(0 + 45*order)
    
    Dragon_2 = Dragon.clone()
    Dragon_2.color('orange')
    Dragon_2.left(90 + 45*order)
    
    Dragon_3 = Dragon.clone()
    Dragon_3.color('green')
    Dragon_3.left(180 + 45*order)
    
    Dragon_4 = Dragon.clone()
    Dragon_4.color('yellow')
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
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()
    
def Dragon_quadruplets_3(order=12, base_length=5, origin=(100,200)):

    name = "Dragon Curve - Quadruplets 3"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(135*order)
    turtle.pendown()

    # Draw first curve:
    turtle.color('blue')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw second curve:
    turtle.color('orange')    
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)
        
    turtle.right(90)

    # Draw third curve:
    turtle.color('green')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw fourth curve: 
    turtle.color('yellow')    
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()
    
def Dragon_quadruplets_4(order=12, base_length=5, origin=(-300,-100)):

    name = "Dragon Curve - Quadruplets 4"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(180 + 135*order)
    turtle.pendown()

    # Draw first curve:
    turtle.color('blue')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.right(90)

    # Draw second curve:
    turtle.color('yellow')    
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)
        
    turtle.right(90)

    # Draw third curve:
    turtle.color('green')    
    for i in range(1<<order):
        if (((i & -i) << 1) & i): turtle.left(90)
        else:                     turtle.right(90)
        turtle.forward(base_length)

    turtle.left(90)

    # Draw fourth curve:
    turtle.color('orange')    
    for i in reversed(range(1<<order)):
        turtle.forward(base_length)
        if (((i & -i) << 1) & i): turtle.right(90)
        else:                     turtle.left(90)

    # Save the drawing:
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()

    
### TERDRAGON CURVES ###########################################################

def Terdragon(order=8, base_length=3, origin=(-400,50)):

    name = "Terdragon Curve"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.color("yellow")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Draw the curve:
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
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()

def Terdragon_triplets(order=8, base_length=3, origin=(-400,50)):

    name = "Terdragon Curve - Triplets"

    # Maximize screen and add a title:
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title(name)

    # Basic turtle set-up
    turtle.bgcolor("black")
    turtle.color("yellow")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    # Move the turtle to the origin:
    turtle.penup()
    turtle.goto(origin)
    turtle.right(30*order)
    turtle.pendown()

    # Draw the first curve:
    turtle.color("green")
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
    turtle.color("yellow")
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
    turtle.color("blue")
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
    #turtle.getscreen().getcanvas().postscript(file=name+".ps")

    # Close the window:
    turtle.exitonclick()


### GOSPER CURVES ##############################################################

def Gosper(order=5, length=4):

    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Gosper curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto((-100,-250))
    turtle.right(30*order)
    turtle.color("yellow")
    turtle.pendown()

    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "A-B--B+A++AA+B-"
            elif char == "B": new_seq += "+A-BB--B-A++A+B"
            else:             new_seq += char
        seq = new_seq

    for char in seq:
        if   char == "-": turtle.right(60)
        elif char == "+": turtle.left(60)
        else:             turtle.forward(length)

    turtle.exitonclick()
        
def Gospers_heptaplets(order=5, length=4):

    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Gosper curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto((-100,-250))
    turtle.right(30*order)
    turtle.pendown()

    seq = "A"
    for i in range(order):
        new_seq = ""
        for char in seq:
            if   char == "A": new_seq += "A-B--B+A++AA+B-"
            elif char == "B": new_seq += "+A-BB--B-A++A+B"
            else:             new_seq += char
        seq = new_seq

    N = len(seq)//7
    colors = ("blue", "green", "yellow", "green", "blue", "green", "blue")
    for i in range(7):
        turtle.color(colors[i])
        for char in seq[i*N: (i+1)*N]:
            if   char == "-": turtle.right(60)
            elif char == "+": turtle.left(60)
            else:             turtle.forward(length)

    turtle.exitonclick()


### FIBONACCI WORD #############################################################

def Fibonacci(order=18, length=3):

    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Fibonacci Word curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto((-400,-200))
    turtle.color("yellow")
    turtle.pendown()

    S, SS  = "0", "01"
    for i in range(order): S, SS = SS, SS+S

    for i, char in enumerate(S):
        turtle.forward(length)
        if char == "0":
            if i%2: turtle.right(90)
            else:   turtle.left(90)   

    turtle.exitonclick()
        
def Fibonacci_tritone(order=18, length=3):

    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Fibonacci Word curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto((-400,-200))
    turtle.right(-90)
    turtle.pendown()

    F, S, SS = [1], "0", "01"
    for i in range(order):
        S, SS = SS, SS+S
        F.append(len(S))

    colors = ("yellow", "green", "orange")

    for i in range(1,len(F)):
        turtle.color(colors[i%3])
        for j in range(F[i-1], F[i]):
            turtle.forward(length)
            if S[j] == "0":
                if j%2: turtle.right(90)
                else:   turtle.left(90)

    turtle.exitonclick()


### HILBERT ####################################################################

def Hilbert(order=6):
    
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Hilbert curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto((-400,-200))
    turtle.color("yellow")
    turtle.pendown()

    hilbert_seq = "a"

    for _ in range(order):
        new_seq = ""
        for char in hilbert_seq:
            if char == "a":
                new_seq += "-bF+aFa+Fb-"
            elif char == "b":
                new_seq += "+aF-bFb-Fa+"
            else:
                new_seq += char
        hilbert_seq = new_seq

    for char in hilbert_seq:
        if char == "F":
            turtle.forward(9)
        elif char == "+":
            turtle.right(90)
        elif char == "-":
            turtle.left(90)

    turtle.exitonclick()


### LEBESGUE ###################################################################

def Lebesgue(order=6, base_length=10, origin=(-350,350)):
    
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Lebesgue curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto(origin)
    turtle.color("yellow")
    turtle.pendown()

    for i in range(1<<(2*order)):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))
            
    turtle.exitonclick()

def Lebesgue_quadruplets(order=6, base_length=10, origin=(-350,350)):
    
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    screen.title("Lebesgue curve")

    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.delay(0)
    turtle.speed(0)

    turtle.penup()
    turtle.goto(origin)
    turtle.pendown()

    N = 1<<(2*order)

    turtle.color("yellow")
    for i in range(0, N//4):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

    turtle.color("green")
    for i in range(N//4, N//2):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

    turtle.color("blue")
    for i in range(N//2, 3*N//4):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

    turtle.color("orange")
    for i in range(3*N//4, N):
        x, y, bit = 0, 0, 1
        while i:
            if i&1: x += bit
            i   /= 2
            if i&1: y += bit
            i   /= 2
            bit *= 2
        turtle.goto((origin[0] + x*base_length, origin[1] - y*base_length))

            
    turtle.exitonclick()


### MAIN FUNCTION ##############################################################

if __name__ == '__main__':

    #Dragon()
    #Dragon_bitone()
    #Dragon_twins_1()
    #Dragon_twins_2()
    #Dragon_quadruplets_1()
    #Dragon_quadruplets_2()
    #Dragon_quadruplets_3()
    #Dragon_quadruplets_4()

    #Terdragon()
    #Terdragon_triplets()

    #Gosper()
    #Gospers_heptaplets()

    #Fibonacci()
    #Fibonacci_tritone()

    #Hilbert()

    #Lebesgue()
    Lebesgue_quadruplets()

################################################################################
