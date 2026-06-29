# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import prettytable

maxi = Turtle()
print(maxi)

# Change shape to turtle
maxi.shape("turtle")

# Change pen color to black and fill color to green
maxi.color("black","green")

# move turtle forward 100 paces
maxi.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Create a blank table
table = prettytable.PrettyTable()
print(table)

# Added one column
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
print(table)

# Added another column
table.add_column("Type",["Electric","Water","Fire"])
print(table)

# Changing style 
print(table.align)