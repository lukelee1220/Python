import turtle
t=turtle

def rectangle(pos,length , width):
    t.up()
    t.goto(pos)
    t.down()
    for n in range(2):
        t.fd(length)
        t.right(90)
        t.fd(width)
        t.right(90)

def triangle(pos,length):
    t.up()
    t.goto(pos)
    t.down()
    t.speed(1)
    t.setheading(60)
    t.fd(length)
    t.circle(length, steps=3)

t.fillcolor("red")
t.begin_fill()
rectangle([0,0],40,20)
t.end_fill()
triangle([100,100],60)

t.setup(600,400)
t.pensize(5)
for i in range(4):
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.goto(0,0)
    t.left(45)
t.done()
