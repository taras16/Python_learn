from turtle import *
from random import randrange as rnd
color('red', 'yellow')
pu() # підняти перо
for x in range(6):
    x = rnd(-200, 200)
    y = rnd(-200, 200)
    setpos(x,y) # задати позицію
    pd() # опусти перо
    begin_fill()
    circle(rnd(10,50))
    end_fill()
    pu()

exitonclick()
done()
