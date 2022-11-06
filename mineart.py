#СУПЕР ДРОУЭР! НАРИСУЕТ МОБА ИЗ МАЙНКРАФТА!!!
import turtle,random
import time
import sys
inp = int(input("Напишите число не больше 5"))
if inp > 5:
    sys.exit()
arr = [0,1,8,27,64,125]
if inp**3 in arr:
    wn = turtle.Screen()
    wn.setup(1000,1000,500,0)
    turtle.bgcolor('red')
    t = turtle.Turtle('square')
    delta=1
    t.shapesize(delta)
    t.penup()
    wn.tracer(4)
    if inp**3 == arr[0]:
        pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,0,0,1,1,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,1,0,0]]
        cls = ['green','black']
    if inp**3 == arr[1]:
        
        pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        cls = ['white','grey']
    if inp**3 == arr[5]:
        
        pixels = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        cls = ['black','grey']
    t.hideturtle()
    def art(x,y):
        for i in range(0,len(pixels)):
            t.goto(x,y-i*20*delta)
            for j in range(0,len(pixels)):
                t.color('grey',cls[pixels[i][j]])
                t.showturtle()
                t.stamp()
                t.fd(20*delta)
        t.hideturtle()
    art(0,0)
