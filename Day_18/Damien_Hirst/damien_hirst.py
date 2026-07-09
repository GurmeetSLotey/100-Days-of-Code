"""Create a painting in the style of Damien Hirst use Turtle"""

from turtle import Turtle, Screen
import random
from colorgram_colors import rgb_colors

screen_height = int(input("Enter canvas height: "))
screen_width = int(input("Enter canvas width: "))

border_height = screen_height / 2 - 30
border_width = screen_width / 2 - 25

num_rows = int(border_height * 2 / 40)
num_columns = int(border_width * 2 / 40)

print(num_columns,num_rows)

starting = (border_width * -1, border_height * -1)

paint_brush = Turtle()
screen = Screen()
screen.setup(width=screen_width, height=screen_height, startx=None, starty=None)
# screen.screensize(canvheight=screen_height, canvwidth=screen_width)
screen.colormode(255)

def random_color():
    return random.choice(rgb_colors)

print(random_color())

paint_brush.up()
paint_brush.goto(starting)

for rows in range(0,num_rows):
    paint_brush.setx(border_height * -1)

    for cols in range(0,num_columns):
        paint_brush.dot(20,random_color())
        paint_brush.setx(paint_brush.xcor()+40)

    paint_brush.dot(20,random_color())
    paint_brush.sety(paint_brush.ycor()+40)

screen.exitonclick()