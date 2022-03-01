#반복문

'''#0~100까지 짝수와 홀수 출력
for i in range(0,101,2):
    print(i)
for i in range(1,100,2):
    print(i)'''

'''#10~1순서로 출력
for i in range(10,1,-1):
    print(i,end="")'''

'''#팩토리얼 만들기
n=int(input("수를 입력하세요"))
fact=1

for i in range(1,n+1):
    fact *= i

print("n!은 ",fact,"이다")'''

'''#0~100까지 합을 while로 출력
count=1
sum=0

while count<=100:
    sum += count
    count += 1

print("1~100까지의 합은",sum,"입니다")
print(count)'''

'''#로그인 프로그램
id=""
passward=""
while id!="gunwoo" or passward!=1234:
    id=input("아이디를 입력하세요")
    passward=int(input("비밀번호를 입력하세요"))
print("로그인을 완료하였습니다")'''

'''#별로 삼각형 만들기
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * * 
#* * * * * * * * *
for i in range(10):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")'''

'''#터틀로 6개 삼각형 만들고 코드 줄이기
import turtle as t
t.shape("turtle")
for i in range(6):
    t.circle(100)
    t.speed(0)
    if i==5:
        break
    t.left(60)'''

'''#도돌이표
print("A B", end=" ")
for i in range(2):
    print("C D", end=" ")'''

'''#랜덤워크 터틀
import turtle as t, random as r
t.shape("turtle")
t.speed(0)

for i in range(30):
    Rnumber=r.randrange(1,51)
    Rangle=r.randrange(-180,180)
    t.setheading(Rangle)
    t.forward(Rnumber)'''

'''#범인 찾기 게임
#3개의 방 중 한 곳에 숨어버린 범인을 찾아라
#범인이 숨은 방을 맞추면 10점 추가 후 방+1하고 다음 스테이지
#30점에 게임 종료
#하지만 게임이 틀리면 범인은 다른 방에 숨고 5점 감점 후 다시 맞추기(0점 이하로 안 내려감)
#시간 체크해서 등급주기
import random as r, time as t

score=0
roomCount=4 #방이 3개
grade=""

start=float(t.time())
while 1:
    n=int(input("범인의 방을 맞추어 주세요(1~3)"))
    room=r.randrange(1,roomCount)

    if n==room:
        score +=10
        roomCount+=1
        print("범인을 체포하였습니다")
    elif n<1 and n>3:
        print("방을 다시 입력 해주세요")
    else : 
        if score !=0:
            score -=5
        print("범인을 놓쳤습니다")

    if score >= 30:
        end=float(t.time())
        break

alltime = end-start
if alltime <10 : 
    grade="A"
elif 10< alltime and alltime <20:
    grade="B"
else : 
    grade="C"

print("게임종료")
print("소요시간은{:.2f}입니다".format(alltime))
print("점수는",grade,"입니다")'''

'''#몬드리안 터틀만들기 : 직사각형 막 만들고 색칠함
import turtle as t, random as r
t.speed(10)

color=["red", "yellow", "green", "blue", "pink", "navy", "purple"]

for i in range(30):
    Xcoordinate=int(r.randrange(0,300))
    Ycoordinate=int(r.randrange(0,300))
    Slength=int(r.randrange(1,151))

    t.penup()
    t.goto(Xcoordinate,Ycoordinate)
    t.pendown()

    t.color(color[r.randrange(0,7)])
    t.begin_fill()
    for j in range(4):
        t.forward(Slength)
        if j==3:
            break
        t.left(90)
    t.end_fill()'''

'''#모든 약수 구하기
answer=int(input("자연수를 입력하시오: "))
for i in range(1,answer+1):
    if answer % i==0:
        print(i,end=" ")'''

'''#뉴클리드 호제법을 사용하여 최대 공약수 구하기
# X와 Y의 최대 공약수
# X=Yx?+Z로 나타 낼 수 있다. 이러한 방법으로 나머지가 없을때 까지 수를 줄여나가라
# 나머지가 없다면 그때의 Y가 최대 공약수이다
B_answer=int(input("큰 수를 입력하시오: "))
S_answer=int(input("작은 수를 입력하시오: "))

while 1:
    rest=B_answer % S_answer

    B_answer=S_answer
    S_answer=rest

    if rest==0:
        print("최대 공약수는",B_answer,"입니다")'''

'''#터틀로 별모양 그리기
import turtle as t

for i in range(5):
    t.forward(80)
    t.left(144)'''
    
#1~100사이의 숫자를 무작위로 추출하여 숫자를 맞추는 게임
import random as r
number=r.randrange(0,101)
count=0

while 1:
    answer=int(input("숫자를 입력해 주세요: "))
    if answer == number:
        print("축하드립니다. 시도횟수",count)
        break
    elif answer > number:
        print("정답보다 높음.")
        count+=1
    elif answer < number:
        print("정답보다 낮음.")
        count+=1
    elif  0 > answer and answer >100:
        print("다시 입력해주세요.")
   

    




        
        
        

