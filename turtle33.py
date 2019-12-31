import turtle
t=turtle
t.screensize(1000000000,100000000, "pink")
t.pensize(5)
t.up()
t.goto(0,0)
t.down()
t.setheading(180)

t.fillcolor("black")
t.begin_fill()
t.circle(50,steps=3)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.up()
t.goto(-40,-80)
t.down()
t.setheading(0)
t.down()
t.setheading(270)
t.forward(270)
t.left(90)
t.forward(80)
t.left(90)
t.forward(270)
t.left(90)
t.forward(80)

t.end_fill()



t.fillcolor("black")
t.up()
t.goto(47,-200)
t.down()
t.begin_fill()
t.setheading(-45)
t.forward(150)
t.right(45)
t.forward(50)
t.right(90)
t.forward(110)
t.end_fill()

t.fillcolor("black")
t.up()
t.goto(-47,-200)
t.down()
#t.left(-135)
t.begin_fill()

t.setheading(-135)
t.forward(150)
t.right(-45)
t.forward(50)
t.right(-90)
t.forward(110)
t.setheading(0)
t.end_fill()



t.done()
