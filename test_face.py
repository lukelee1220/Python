def draw(x,y):
    import turtle
    t=turtle.Pen()
    t.hideturtle()
    
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
    t.goto(-15,60)
    t.down()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.up()
    t.goto(25,62)
    t.down()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.up()
    t.pensize(10)
    t.goto(-25,40)
    t.down()
    t.goto(-10,20)
    t.goto(10,20)
    t.goto(25,40)
    turtle.done()

a=int(input("你要画几个笑脸"))
for i in range(a):
    x=int(input("input the x number"))
    y=int(input("input the y number"))
    draw(x,y)