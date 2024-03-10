# Если в задании просят посчитать кол-во точек входящих в одну фигуру и не входящих в другую,
# то надо считать разность между количеством точек внутри одной фигуры и другой без учета границ 

from turtle import *
import keyboard
koff_mash = 10
povtor = 4
correction = 1
color("green")
left(90)
begin_fill()

for i in range(povtor):
    forward(9*koff_mash)
    right(90)
    print(position())
end_fill() 
penup()

cnt = 0
canvas = getcanvas()
for x in range(-100*koff_mash,100*koff_mash,koff_mash):
    for y in range(-100*koff_mash,100*koff_mash,koff_mash):
        s = canvas.find_overlapping(x,y,x,y)
        if len(s) == 1 : 
            cnt+=1
            print(s, x, y)
print(cnt)      

canvas.delete('all') 
begin_fill()
color("red")
for i in range((povtor- correction)):
    forward(9*koff_mash)
    right(120)
    print(position())
end_fill()  

penup()
cnt = 0
canvas = getcanvas()
for x in range(-100*koff_mash,100*koff_mash,koff_mash):
    for y in range(-100*koff_mash,100*koff_mash,koff_mash):
        s = canvas.find_overlapping(x,y,x,y)
        if len(s) == 1: 
            cnt+=1
            print(s, x, y)
print(cnt)      
keyboard.read_key()