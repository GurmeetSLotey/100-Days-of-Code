from turtle import Turtle, Screen
import random 

timmy = Turtle()
screen = Screen()
screen.colormode(255) # To change the color mode for RGB

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(degree):
    for _ in range(int(360/degree)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + degree)

timmy.speed("fastest")

draw_spirograph(10)



screen.exitonclick()