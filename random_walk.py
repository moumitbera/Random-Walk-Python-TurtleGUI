import turtle as turt
import random
turt.colormode(255)
turtle = turt.Turtle()

turtle.pensize(10)

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return (red, green, blue)


degrees = [0, 90, 180, 270]

turtle.speed("fastest")

def move():
    color = random_color()
    turtle.pencolor(color)
    turn_deg = random.choice(degrees)
    turtle.setheading(turn_deg)
    turtle.fd(20)


for i in range(300):
    move()

screen = turt.Screen()
screen.exitonclick()