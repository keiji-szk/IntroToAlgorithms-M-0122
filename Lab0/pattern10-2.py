import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(2)
t.speed(0)

for i in range(30):
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(90)
    t.pencolor("blue")
    t.circle(60)
    t.pencolor("red")
    t.circle(100)
    t.penup()
    t.goto(0, 0)
    t.left(90)
    t.left(12)


screen.exitonclick()
