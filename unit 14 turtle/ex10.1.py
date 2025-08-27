import turtle
import random

# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

turtle.colormode(255)
# Turtle Pen
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.speed(10)
pen1.color("yellow")
pen1.width(25)  # more
# pen1.fillcolor(219, 96, 97)
r=random.randint(0,219)
b=random.randint(0,116)
g=random.randint(0,147)


pen1.fillcolor(r, g, b)

pen2.speed(10)
pen2.color("blue")
pen2.width(10)  # less

# Draw the "G"
pen1.begin_fill()
pen1.circle(100, 360)  # yellow
pen1.end_fill()

pen2.begin_fill()
pen2.circle(100, 360)  # blue
pen2.begin_fill()

pen2.penup()
pen2.goto(30, 100)  # x,y right(30), up(100)
pen2.pendown()
pen2.fillcolor('white')
pen2.begin_fill()
pen2.circle(30, 360)
pen2.end_fill()

pen2.fillcolor('black')
pen2.begin_fill()
pen2.circle(10, 360)
pen2.end_fill()

pen2.penup()
pen2.goto(-40, 100)
pen2.pendown()

pen2.fillcolor('white')
pen2.begin_fill()
pen2.circle(30, 360)
pen2.end_fill()

pen2.fillcolor('black')
pen2.begin_fill()
pen2.circle(10, 360)
pen2.end_fill()


diff=random.randint(-30,30)
pen2.penup()
pen2.goto(-10, 45)
pen2.circle(30, -60)
pen2.pendown()
pen2.circle(30, -120)

# Hide the turtle
pen1.hideturtle()
pen2.hideturtle()

# Keep window open
screen.mainloop()
