import turtle
# Setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Turtle
t0 = turtle.Turtle() #drawing pencil
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t.hideturtle()
t0.hideturtle()
t1.hideturtle()
t2.hideturtle()


t0.speed(2)
t0.color("red")
t0.width(27)
t.speed(2)
t.color("yellow")
t.width(27)
t2.speed(2)
t2.color("blue")
t2.width(27)
t1.speed(2)
t1.color("green")
t1.width(28)


# Draw the "G"                                deg
t0.circle(100, -200) #(100=radius(size ),-200(forward) opposite'-')
t.circle(100, -80)
t1.circle(100, -40)
t2.circle(100, 90)

t2.right(90)
t2.backward(110)

# Hide the turtle


# Keep window open
screen.mainloop()
