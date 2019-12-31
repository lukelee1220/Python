import turtle

turtle.color("red", "green")
turtle.begin_fill()

turtle.goto(200,0)
turtle.goto(200,200)
turtle.goto(0,200)
turtle.goto(0,0)
turtle.end_fill()


turtle.penup()
turtle.goto(100,100)
turtle.pendown()

turtle.color("red", "blue")
turtle.begin_fill()
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.end_fill()


turtle.color("red", "blue")
turtle.begin_fill()
turtle.goto(200,200)
turtle.goto(200,0)
turtle.goto(100,-100)
turtle.goto(100,100)
turtle.end_fill()

turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(200,0)



turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(0,200)

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.goto(0,0)


turtle.done()
