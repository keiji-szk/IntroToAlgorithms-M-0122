import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

t.color("blue")
t.pensize(2)
# polygons
for j in range(10):
    for i in range(10):
        t.forward(70)
        t.left(36)
    t.left(36)

t.color("red")
for j in range(10):
    for i in range(5):
        t.forward(140)
        t.left(72)
    t.left(36)

screen.exitonclick()
