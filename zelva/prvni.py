from math import sqrt
from turtle import forward, left, exitonclick, right
from random import randint


def domecek(a):
    c = sqrt(a*2**a)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    
for i in range(10):
    domecek(randint(10,20))
    right(36)

exitonclick()