import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()
t.shape("turtle")
'''
#삼각형 그리기
t.forward(100)
t.left(150)
t.forward(50)
t.left(60)
t.forward(50)

#한번도 안 때고 집모양 그리기
t.forward(80)
t.left(135)
t.forward(110)
t.right(135)
t.forward(80)
t.right(135)
t.forward(110)
t.right(135)
t.forward(80)
t.right(45)
t.forward(55)
t.right(90)
t.forward(55)
t.right(45)
t.forward(80)

#오륜기 그리기
t.speed(0)

t.circle(100)
t.penup()
t.goto(50,0)
t.pendown()
t.circle(100)
t.penup()
t.goto(100,0)
t.pendown()
t.circle(100)
t.penup()
t.goto(75,-50)
t.pendown()
t.circle(100)
t.penup()
t.goto(25,-50)
t.pendown()
t.circle(100)
'''
#여러 색의 다각형 그리기
turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5








