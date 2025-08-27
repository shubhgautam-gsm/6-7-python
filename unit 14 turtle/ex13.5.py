import turtle
import random

def draw_face():
    # Set up turtle
    turtle.penup()
    turtle.speed(0)  # Set maximum drawing speed
    turtle.width(2)  # Set pen width

    # Draw face
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.fillcolor("peachpuff")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    # Draw left eye
    turtle.penup()
    turtle.goto(-40, 20)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw right eye
    turtle.penup()
    turtle.goto(40, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw left pupil(kiki)
    turtle.penup()
    turtle.goto(-30, 30)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw right pupil(kiki)
    turtle.penup()
    turtle.goto(30, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # Draw nose
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.width(4)
    turtle.goto(0, -20)

    # Draw mouth
    turtle.penup()
    turtle.goto(-40, -40)
    turtle.pendown()
    turtle.width(2)
    turtle.right(90)
    turtle.circle(40, 180)
    turtle.penup()

   
def generate_face():
    turtle.reset()
    draw_face()
    turtle.hideturtle()  # Hide the turtle cursor

def main():
    turtle.setup(width=400, height=400)
    turtle.Screen().bgcolor("lightblue")

    generate_face()

    turtle.done()

if __name__ == "__main__":
    main()
