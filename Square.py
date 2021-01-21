import turtle as t
import time

pen = t.Turtle()
pen.color("cyan")
pen.speed(0)

def karecizim():
        for side in range(4):
                pen.forward(100)
                pen.right(90)
                for side in range(4):
                        pen.forward(50)
                        pen.right(90)

pen.penup()
pen.back(20)
pen.pendown()

for square in range(80):
        karecizim()
        pen.forward(5)
        pen.left(5)
        
pen.hideturtle()

time.sleep(10)