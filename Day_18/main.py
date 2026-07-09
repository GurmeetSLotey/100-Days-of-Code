from turtle import Turtle, Screen
import random 

colors = ["red","blue","green","wheat","black"]
degrees = [0,90,180,270]

def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def draw_dash(turtle, distance):
    for _ in range(10):
        turtle.forward(distance)
        turtle.up()
        turtle.forward(distance)
        turtle.down()

def draw_multiple_shapes(n):
    for i in range(3,n+1):
        degree = 360/i
        timmy.color(random.choice(colors))
        for _ in range(i):
            timmy.forward(100)
            timmy.right(degree)

def random_walk():
    timmy.pensize(10)
    for _ in range(50):
        timmy.color(random.choice(colors))
        timmy.setheading(random.choice(degrees)) # using setheading as it makes it look sharper of turns
        timmy.forward(25)

def reset_screen():
    timmy.home()
    timmy.clear() # needs to be timmy and not screen
    # timmy.showturtle()
    timmy.shape("arrow")

timmy = Turtle()
timmy.speed("fast")
screen = Screen()
screen.colormode(255) # To change the color mode for RGB


timmy.shape("turtle")
timmy.color("red")

draw_square(timmy)

reset_screen()

# draw_dash(timmy,10)

reset_screen()

# draw_multiple_shapes(10)

reset_screen()

# Random walk
random_walk()

screen.exitonclick()