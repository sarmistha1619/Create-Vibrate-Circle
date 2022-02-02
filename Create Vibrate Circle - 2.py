import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("gray")
a = 10
b = 50

while True:
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1

    if b== 200:
        break

    t.hideturtle()
