import turtle 

loadWindow = turtle.Screen()
turtle.speed(20)
turtle.colormode(255)
for i in range(200):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
   
    b = i 
    if b >51:
        b = 51
    turtle.color(i, 2*i ,5*i)

turtle.exitonclick()


