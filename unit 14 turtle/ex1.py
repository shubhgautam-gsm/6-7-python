import turtle

window = turtle.Screen()
window.setup(height=600,width=700)
pen = turtle.Turtle()

# Draw vertical line
pen.left(90)  # Turn left to face upward
pen.forward(110)
pen.left(90)
pen.forward(110)
pen.left(90)  # Turn left to face upward
pen.forward(110)
pen.left(90)
pen.forward(110)

turtle.done() # not exit the box