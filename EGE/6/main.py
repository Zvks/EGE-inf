from turtle import *
import keyboard
koff_mash = 20
povtor = 16
left(90)
for i in range(povtor):
    right(60)
    forward(2*koff_mash)
    right(60)
    forward(2*koff_mash)
    right(270)

penup()
for x in range(-8, 15):
    for y in range(-20, 8):
        setpos(x*koff_mash, y*koff_mash)
        dot(4, 'red')
keyboard.read_key()