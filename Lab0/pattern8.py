import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.right(36)

for i in range(19):
    t.forward(190 - i * 10)
    t.left(144)

t.penup()
t.forward(200)
screen.exitonclick()
