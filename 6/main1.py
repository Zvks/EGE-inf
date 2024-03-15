from turtle import *

koff_mash = 20
povtor = 2
correction = 0

color("green")
left(90)
begin_fill()
for i in range(povtor-correction):
    forward(17*koff_mash)
    left(90)
    forward(10*koff_mash)
    left(90)
penup()
end_fill()
backward(4*koff_mash)
right(90)
backward(3*koff_mash)
left(90)
pendown()
begin_fill()
for i in range(povtor-correction):
    forward(40*koff_mash)
    right(90)
    forward(10*koff_mash)
    right(90)
end_fill()
penup()

cnt = 0
canvas = getcanvas()
for x in range(-100*koff_mash, 100*koff_mash, koff_mash):
    for y in range(-100*koff_mash, 100*koff_mash, koff_mash):
        s = canvas.find_overlapping(x,y,x,y)
        if len(s) > 0:
            print(s)
            cnt += 1
print(cnt)