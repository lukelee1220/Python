import turtle

t=turtle
radius = 100
t.screensize(40,40, "green")
t.pensize(5)

def face(x, y):
    if(x>400 or y>400):
        print("input error")
    #pencolor & fillcolor
    t.color("red", "yellow")
    t.penup()
    t.home()

    t.goto(x,y)
    t.pendown()
    
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    #left eye
    t.penup()
    print(x-50,y+radius+30)
    t.goto(x-50,y+radius+30)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)

    #right eye
    t.penup()
    t.forward(100)
    t.pendown()
    t.circle(10)
    t.end_fill()

    #mouth
    t.penup()
    t.goto(x-25,y+50)
    t.pendown()
    t.right(60)
    t.circle(25, 120)
    t.left(60)

    #nose
    t.penup()
    t.goto(x+10,y+100)
    t.pendown()
    t.circle(20,steps=3)
    
#
# for x in range(0,200,50):
#     for y in range(0,200, 50):
#         face(x,y)
face(0,0)
face(-150,-200)
face(40,100)
t.hideturtle()

t.mainloop()
