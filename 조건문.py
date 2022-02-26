#조건문

'''#암호문 만들기
cord = input("암호 입력")
print(cord[-1:-9:-1])
#cord[-1:비어있으면 끝까지감:-1]'''

'''#2050년 나는 몇살?
import time
now=time.time()
thisYear=int(1970+now//(3600*24*365))
print("올해는",thisYear, "입니다")
age=int(input("당신의 나이를 입력하세요: "))
print("2050년 에는",int(age+28),"살이군요")'''

'''#if문 예제
language = int(input("언어를 선택하세요(1.한국어 2.영어 3.프랑스어 4.독일어)"))
if language ==1:
    print("안녕")
elif language ==2:
    print("hello")
elif language ==3:
    print("Bonjour")
else :
    print("구텐몰겐")'''

'''#직각삼각형 판별하기
a=int(input("a의 길이는?"))
b=int(input("b의 길이는?"))
c=int(input("c의 길이는?"))
if c**2==a**2+b**2:
    print("직각삼각형 입니다")
else :
    print("직각삼각형이 아닙니다")'''

'''#정수의 종류를 판별하는 터틀
import turtle as t
t.shape("turtle")
t.penup()
t.goto(100,100)
t.write("입력된 정수는 양의 정수입니다")
t.goto(100,0)
t.write("입력된 정수는 0입니다")
t.goto(100,-100)
t.write("입력된 정수는 음의 정수입니다")
t.goto(0,0)
t.pendown()
answer=int(t.textinput("입력창","정수를 입력해 주세요"))
if answer>0:
    t.left(45)
    t.forward(100)
elif answer==0:
    t.forward(100)
else :
    t.right(45)
    t.forward(100)'''

'''#주민번호 뒷자리로 남녀 판별하기
import random as r
number = r.randrange(1,5)
print("주민등록번호의 성별 정보 번호를 생성합니다.")
print("생성번호",number)
if number == 1 or number == 3:
    print("남자입니다")
else :
    print("여자입니다")'''

'''#동전 던지기
import turtle as t, random as r

screen = t.Screen()
image1 = "1.gif"
image2 = "2.gif"

screen.addshape(image1)
screen.addshape(image2)

coin = r.randrange(0,2)

if coin ==0:
    t.shape(image1)
    t.stamp()
else :
    t.shape(image2)
    t.stamp()'''

'''#직렬연결vs병렬연결(병렬연결만 1개만 연결되도 불이 켜짐)
a=input("1번 전지가 있습니까?(y/n)")
b=input("2번 전지가 있습니까?(y/n)")
if not (a=="n" and b=="n") : 
    if a=="y" and b=="y" :
        print("직렬연결 : 전구에 불이 켜집니다")
        print("병렬연결 : 전구에 불이 켜집니다")
        exit
    print("직렬연결 : 전구에 불이 꺼집니다")
    print("병렬연결 : 전구에 불이 켜집니다")
else : 
    print("직렬연결 : 전구에 불이 꺼집니다")
    print("병렬연결 : 전구에 불이 꺼집니다")'''

'''#판별식
a=float(input("a값 입력"))
b=float(input("b값 입력"))
c=float(input("b값 입력"))
D=(b**2)-4*a*c
if D>0:
    print("두 실근 입니다")
elif D==0:
    print("중근 입니다")
else :
    print("두 허근 입니다")'''

'''#사용자가 원하는 도형을 터틀로 그리기
import turtle as t
answer = t.textinput(" ","도형을 입력하시오")
if answer == "직사각형":
    width=int(t.textinput(" ","가로"))
    height=int(t.textinput(" ","세로"))
    t.shape("turtle")
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
elif answer == "정삼각형":
    lenght=int(t.textinput(" ","한 변의 길이"))
    t.shape("turtle")
    t.forward(lenght)
    t.left(120)
    t.forward(lenght)
    t.left(120)
    t.forward(lenght)
else :
    t.shape("turtle")
    radius=int(t.textinput(" ","반지름의 길이"))
    t.circle(radius)'''

#두 원의 위치관계(입력은 정수만)
import turtle as t
x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
radius1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
radius2 = int(input("작은 원의 반지름: "))
t.shape("turtle")

distance = ((x2-x1)**2+(y2-y1)**2)**0.5

if distance == 0:
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("동심원")
elif distance == radius2-radius1:
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("내접")
elif distance == radius2+radius1:
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("외접")
elif distance > radius2+radius1 :
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("두 원이  밖에서 떨어진 경우")
elif distance > radius2-radius1:
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("두 원이  안에서 떨어진 경우")
else :  #radius2+radius1 < distance and distance < radius2+radius1:
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.circle(radius1)
    t.penup()
    t.goto(x2,y2)
    t.pendown()
    t.circle(radius2)
    t.write("두 원이  두 점에서 만나는 경우 경우")
