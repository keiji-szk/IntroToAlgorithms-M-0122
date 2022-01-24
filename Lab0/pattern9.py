import turtle
screen = turtle.Screen()
ryan = turtle.Turtle()
ryan.shape("turtle")

ryan.color("blue")
ryan.pensize(2)
# polygons
for j in range(10):
    for i in range(10):
        ryan.forward(70)
        ryan.left(36)
    ryan.left(36)

ryan.color("red")
for j in range(10):
    for i in range(5):
        ryan.forward(140)
        ryan.left(72)
    ryan.left(36)

screen.exitonclick()
