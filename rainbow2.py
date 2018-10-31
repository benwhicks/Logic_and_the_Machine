from turtle import *

# this makes the turtle go fast
hideturtle()
speed(0)

for n in range(1,180):
    if n%2 == 0:
        color("#aa6622")
    if n%3 == 0:
        color("#005534")
    if n%4 == 0:
        color("#990066")
    if n%5 == 0:
        color("#ab3211")
    forward(100)
    backward(100)
    left(1)
    
done()
