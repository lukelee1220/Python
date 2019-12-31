
# -*- coding: utf-8 -*-
import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)#rad画圆轨迹半径的长度
        turtle.circle(-rad,angle)#angle沿着远行爬行的弧度值
    turtle.circle(rad, 40)
    turtle.fd(rad)#向前爬行rad
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
 
def main():
    turtle.setup(1300,800,0,0)#长为1300，宽为800的窗口，（0,0）窗口左上角在屏幕中的位置
    pythonsize=30#30px
    turtle.pensize(pythonsize)#轨迹宽度
    turtle.pencolor("blue")#轨迹颜色
    turtle.seth(-40)#出发角度
    drawSnake(40,80,5,pythonsize/2)
    turtle.done()
main()
