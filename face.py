import turtle
t=turtle
t.speed(0)
t.screensize(40,40, "pink")
t.pensize(5)

def draw(x,y):
    t.hideturtle()
    
    t.up()
    t.goto(x,y)
    t.down()
    t.color("yellow","yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
    t.goto(x-15,y+60)
    t.down()
    t.color("blue","red")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.up()
    t.goto(x+25,y+62)
    t.down()
    t.color("blue","red")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.pensize(12)
    t.pencolor("black")
    t.up()
    t.setpos(x-25,y+40)
    t.down()
    t.pendown()
    t.right(60)
    t.circle(25, 120)
    t.left(60)

    t.up()
    t.goto(-100,100)
    t.down()
    t.pensize(20)
    d=['red','orange','yellow','green','cyan','blue','purple']
    i=200
    for a in d:
        i-=20

        t.up()
        t.goto(i,0)
        t.down()
        t.pencolor(a)
        t.setheading(90)
        t.circle(i,180)
    
        



# a=int(input("你要画几个笑脸"))
# for i in range(a):
#     x=int(input("input the x number"))
#     y=int(input("input the y number"))
draw(0,-50)
t.mainloop()


    






    
