import turtle
screen = turtle.Screen()
ryan = turtle.Turtle()
ryan.shape("turtle")
ryan.color("black")
ryan.right(36)

for i in range(19):
    ryan.forward(190 - i * 10)
    ryan.left(144)

ryan.penup()
ryan.forward(200)
screen.exitonclick()
