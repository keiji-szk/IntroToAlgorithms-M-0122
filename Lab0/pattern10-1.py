import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(2)
t.speed(0)

for i in range(20):
    t.color("blue")
    t.circle(60)
    t.right(180)
    t.color("red")
    t.circle(100)
    t.right(180)
    t.penup()
    t.forward(5)
    t.pendown()
    t.left(18)

screen.exitonclick()