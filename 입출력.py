'''name = input("이름을 입력하세요: ")
print(name,"씨 안녕하세요")
print("파이썬에 오신것을 환영합니다")'''


'''x=int(input())
y=int(input())
sum=x+y
print(sum)'''

'''
import turtle
t=turtle.Turtle()
t.shape("turtle")

radius = int(input("반지름을 입력해주세요"))
color = input("색을을 입력해주세요")

t.speed(0)

t.color(color)
t.begin_fill()
t.circle(radius)
t.end_fill()
'''

'''
#거리 = 속도*시간
time = int(input("번개가 치고, 몇 초 후에 소리가 들렸는가?"))
print("번개의 장소는",time*340,"m이다")
'''

'''
#섭씨온도=(화씨온도－32)×5/9
#화씨온도 구하기
Stemperture = float(input("섭씨온도"))
Htemperture = float(Stemperture*9/5+32)
print("{:.4f}".format(Htemperture))
'''

'''
#두 점 사이의 거리 구하기
# 루트 : **1/2
x1=float(input("좌표를 입력해주세요"))
x2=float(input("좌표를 입력해주세요"))
y1=float(input("좌표를 입력해주세요"))
y2=float(input("좌표를 입력해주세요"))
l=float((((x2-x1)**2)+((y2-y1)**2))**0.5)
print("{:.2f}".format(l))

'''

'''
#직각삼각형 만들
import turtle
t=turtle.Turtle()
t.shape("turtle")

t.left(45)
t.forward(141.4)
t.setheading(225)
t.forward(141.4)
t.left(135)
t.forward(100)
t.left(90)
t.forward(100)
'''


#표준시간 구하기
import time
'''
fseconds =time.time() #1970년 1월 1일 0시 0분 0초 기준으로 흐른 시간(분단위)
total_sec= int(fseconds//60) # 전체 초단위
total_min =int(total_sec//60) # 전체 분단위
minute = int(total_min%60) #현재 분단위(현재시간은 이러한 규칙! 원리이해x)
total_hour=int(total_min//60) # 전체 시단위
minute = int(total_hour%24) #현재 시단위(현재시간은 이러한 규칙! 원리이해x)
'''
'''
fseconds = 100000
total_hour =fseconds//3600
total_hour_rest=fseconds%3600
total_min= total_hour_rest//60
total_min_rest=total_hour_rest%60
second =total_min_rest%60

print("{}시간{}분{}초".format(total_hour, total_min, second))
'''

'''
price = 10000
print("상품 가격은 %.2f원 입니다"%price)
'''

"""
poem = "이렇게 정다운\n너 하나 나하나는\n어디서 무엇이 되어\n다시 만나랴"
print(poem)
poem = '''이렇게 정다운
너 하나 나하나는
어디서 무엇이 되어
다시 만나랴'''
print(poem)
"""

'''
s="hello python"
print(s[3:8])
print(s[-8:-12:-1])
print(s[7:11])
'''

'''
#챗봇
print("안녕하세요")
name = input("이름이 뭐예요?")
print("만나서 반갑습니다 %s님"%name)
print(name,"이름의 길이는 다음과 같군요:",len(name))
age = int(input("나이가 어떻게 돼요?"))
print("내년이면",age+1,"세가 되시는 군요")
'''

#거북이 인사
import turtle as t
t.shape("turtle")

name = t.textinput("","이름을 입력하세요")
t.write(str(name)+"만나서 반갑습니다")
t.setheading(180)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
