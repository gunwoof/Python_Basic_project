#딕셔너리

'''#전화번호부
phone_book = {"홍길동" : "010-1234-1234", 
            "강감찬" : "010-2145-1234", 
            "이순신" : "010-1234-7834"}

for key in sorted(phone_book.keys()) : 
    print(key, phone_book[key])

print(phone_book)'''

'''#사전 추가
english_dict={}
english_dict["one"] ="하나"
english_dict["two"] ="둘"
english_dict["three"] ="셋"

word=input("단어를 입력하세요")
print(english_dict[word])'''

'''#편의점 재고 관리
items={"커피" : 7, "펜" : 3, "종이컵" : 5, "우유" : 6, "콜라" : 4, "라면" : 11,}

print("판매 전 재고", items)

sell = input("판매한 물건을 입력하세요 : ")

if sell in items:
    items[sell] -= 1
else : 
    print("판매 제품이 아닙니다")

print("판매 후 재고", items)'''

'''#딕셔너리와 반복문
phone_book = {"홍길동" : "010-1234-1234", 
            "강감찬" : "010-2145-1234", 
            "이순신" : "010-1234-7834"}

for k, v in phone_book.items():
    print("{}의 전화번호느 {}입니다".format(k,v))

print(phone_book)'''

'''#행성까지의 여행시간은?
import time as t
planet={"수성":91700000, "금성":41400000, "화성":78400000, "목성":628700000, "토성":1277400000, "천황성":2750400000, "해왕성":4347400000}
name=input("행성이름은?: ")
number=int(input("이동속도는?: "))
time=int(planet[name]/number)
Ytime=time//(365*24)
Mtime=(time%(Ytime*365*24))//(30*24)
Dtime=(time-(Ytime*365*24)-(Mtime*30*24))//(24)
Htime=(time-(Ytime*365*24)-(Mtime*30*24)-(Dtime*24))

print("약 {}년 {}월 {}일 {}시간".format(Ytime,Mtime,Dtime,Htime))'''

'''#멘델의 유전 법칙 시뮬레이션
import random as r
bean=["RR", "Rr", "rR", "rr"]
make_decendant=[]
a=0
b=0
for i in range(10000):
    make_decendant.append(bean[r.randrange(0,4)])

for i in range(10000):
    if make_decendant[i] == "rr":
        a +=1
    else :
        b +=1

print(b/a, ":1")'''

'''#튜링상 수상자 데이터 분석(리스트+딕셔너리)
winner=[]
winner.append({"이름":"팀버너스리", "수상년도":"2016", "국적":"영국", "대표업적":"www개발"})
winner.append({"이름":"리처드 해밍", "수상년도":"1968", "국적":"미국", "대표업적":"오류검출"})
winner.append({"이름":"에츠허르 데이크스트라", "수상년도":"1972", "국적":"네덜란드", "대표업적":"최단거리 알고리즘"})
winner.append({"이름":"더글러스 엥겔바트", "수상년도":"1997", "국적":"미국", "대표업적":"마우스"})
winner.append({"이름":"데니스 리치", "수상년도":"1983", "국적":"미국", "대표업적":"c언어 개발"})

for winners in winner:
    print(winners)'''

#email보내기
import smtplib
from email.mime.text import MIMEText

me="gunwoof1234@gmail.com"
you="gunwoof1234@gmail.com"

contents="오는은 1월 24일"
msg=MIMEText(contents, _charset="euc-kr")
msg["subject"]="수업시간"

msg["form"] =me
msg["to"] =you

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("gunwoof1234", "rjsdndi0625#")

server.sendmail(me, you, msg.as_string())
server.quit
