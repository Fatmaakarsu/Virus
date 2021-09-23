from turtle import *

a = 0
b = 0

bgcolor("black")
pencolor("#3a6f1e")
speed(-2)
penup()
goto(0,-150)
pendown()
begin_fill()
while True:
    forward(a)
    left(b)

    a+=3
    b+=1

    if b==200:
        break
end_fill()
done()