

#함수

'''#터틀로 사각형 만드 코드로 함수를 만듬
import turtle as t
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        if i==3:
            break
        t.left(90)
    
for i in range(4):
    square(100)
    t.penup()
    t.goto(-200*(i+1),0)
    t.pendown()
    t.setheading(0)'''
    
'''#키워드 인수를 사용한 뒤에는 모두 키워드 인수를 사용
def func(x, y, z):
    return x*y*z

print(func(x=1,20,z=50)) // #2번째 인자에 위치인수를 집어 넣어서 오류'''

'''#bmi계산기
height=int(input("키를 입력하세요"))
weight=int(input("몸무게를 입력하세요"))

def bmi(height,weight):
    a=weight/height*height
    if a<18.5:
        print("저체중입니다")
    elif 18.5<=a and a<22.9:
        print("정상입니다")
    elif 23<a and a<24.9:
        print("과체중입니다")
    elif 25<a and a<29.9:
        print("경도비만입니다")
    else:
        print("고도비만입니다")'''

'''#환전 계산기
country=["미국","일본","유럽","중국"]
unit=["달러","앤","유로","위안"]
rate=[1182.5, 169.22, 1286.74, 1078.14]

answer1=int(input("환전금액을 입력하세요"))
answer2=input("국가를 입력하세요")
answer2_1=answer2 #input창 제외하기 위해
answer3=(rate[country.index(answer2)])


def exchange(answer1, answer3):
    return answer1/answer3

print(answer1,"원은",exchange(answer1, answer3),unit[country.index(answer2_1)],"입니다")'''

'''#클릭하는 곳에 사각형 그리기
import turtle as t, random as r
t.shape("turtle")
color=["red", "yellow", "blue", "purple", "gray"]

def square(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    c=r.randrange(0,5)
    t.color(color[c])
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        if i==3:
            break
        t.left(90)
    t.end_fill()
    

t.onscreenclick(square)'''

'''#2차함수 그리기
import turtle as t, random as r
t.shape("turtle")

t.speed(0)
t.penup()
t.goto(-200,0)
t.pendown()
t.forward(400)
t.setheading(90)
t.penup()
t.goto(0,-200)
t.pendown()
t.forward(400)
t.penup()
t.goto(0,0)
t.pendown()

def draw1(x):
   y=(x)**2
   t.goto(x,y)

def draw2(x):
   y=(x)**2
   t.goto(-x,y)

    
for i in range(50):
    draw1(i)
for i in range(50):
    draw2(i)'''

#터틀로 미로 탈출게임 만들기
import turtle as t
t.shape("turtle")

t.speed(0)

t.penup()
t.goto(-300,300)
t.pendown()
t.forward(300)
t.right(90)
t.forward(300)
t.left(90)
t.forward(300)

t.penup()
t.goto(-300,150)
t.pendown()
t.forward(150)
t.right(90)
t.forward(300)
t.left(90)
t.forward(450)

t.penup()
t.goto(-300,225)
t.pendown()

def UP():
    t.setheading(90)
    t.forward(10)

def DOWN():
    t.setheading(270)
    t.forward(10)

def LEFT():
    t.setheading(180)
    t.forward(10)

def RIGHT():
    t.setheading(0)
    t.forward(10)
    
t.listen()
t.onkey(UP,"Up")
t.onkey(DOWN,"Down")
t.onkey(LEFT,"Left")
t.onkey(RIGHT,"Right")







    






