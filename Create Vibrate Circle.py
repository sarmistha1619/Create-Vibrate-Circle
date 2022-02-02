import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("green")
a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1

    if b== 200:
        break

    t.hideturtle()
