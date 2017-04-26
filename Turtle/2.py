from turtle import *
color('green')
width(5) 
speed(10)
pu()


def fig(n):
    pu()
    for r in range(n):
        for z in  range(n):
            fd(10)
            dot()
        fd(-10*n)
        fd(90)
        fd(10)
        rt(-90)
       
fig(10)
fig(3)
done()
exitonclikc()  
print(taras) 