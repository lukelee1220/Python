print("hello ward")
import turtle

turtle.fillcolor("green")
turtle.begin_fill()
for a in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
turtle.up()
turtle.goto(100,-100)
turtle.down()
turtle.fillcolor("blue")
turtle.begin_fill()
for a in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
turtle.left(90)
turtle.forward(200)
turtle.left(45)
turtle.forward(140)
turtle.up()
turtle.goto(100,-100)
turtle.down()
turtle.goto(0,0)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.up()
turtle.goto(300,100)
turtle.down()
turtle.goto(200,200)
turtle.end_fill

turtle.shape("turtle")
turtle.done()