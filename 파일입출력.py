#파일

'''#파일을 read()로 읽어서 출력
infile=open("C:\\Users\ASUS\Desktop\phone.txt","r", encoding='UTF8')
lines=infile.read()
print(lines)
infile.close()'''

'''#한 줄을 읽을때 \n을 없애기(rstrip()사용)
infile=open("C:\\Users\ASUS\Desktop\phone.txt","r", encoding='UTF8')
lines=infile.readline().rstrip()
while lines !="":
    print(lines)
    liens = infile.readline().rstrip()
infile.close()'''


'''infile=open("C:\\Users\ASUS\Desktop\phone.txt","r", encoding='UTF8')
line=infile.readline().rstrip()
for line in infile:
    line=line.rstrip()
    print(line)
infile.close()'''

'''#파일을 write()로 써서 출력
outfile=open("C:\\Users\ASUS\Desktop\phone.txt","a", encoding='UTF8')

outfile.write("홍길동 010-3932-6998\n")
outfile.write("김영희 010-7894-5612\n")
outfile.write("김철수 010-1234-5678\n")

outfile.close()'''

'''#csv파일
import csv
f=open("C:\\Users\ASUS\Desktop\input.csv","r",errors='ignore')
data=csv.reader(f)

for line in data:
    print(line)

f.close()'''

'''#연설문 데이터 분석
infile=open("C:\\Users\ASUS\Desktop\input.txt","r",encoding='UTF8')
line=infile.read()
sortLine=line.lower().replace(",","").replace("-","").split()

ldic={}

for i in sortLine:
    if i in ldic.keys():
        ldic[i]+=1
    else :
        ldic[i]=1

a=len(ldic) #단어 총 개수
#print(ldic)

i=0
j=""
max=-1
maxk=""
for j,i in ldic.items():
    if i>max:
        max=i
        maxk=j
print(max, maxk)

min=100
mink=""
for j,i in ldic.items():
    if i<min:
        min=i
        mink=j
print(min,mink)


infile.close()'''

'''#평균 강수량 통계
infile=open("C:\\Users\ASUS\Desktop\\rain.csv","r")
line=infile.read()
sortLine=line.replace(","," ").replace("100"," ").split()

Sum=0
for i in range(1,len(sortLine),2):
    sortLine[i]=float(sortLine[i])
    Sum +=sortLine[i]

average=Sum/(len(sortLine)/2)

print(Sum)
print(average)'''

#행맨(중복단어 체크 부족)
import random as r, time as t
infile=open("C:\\Users\ASUS\Desktop\\hangman.txt","r")
line=infile.read().split()
quize=r.choice(line)
blank=[]

for i in range(len(quize)):
    blank.append("'_'")

start=t.time()
while 1:
    answer=input("단어를 추측하세요: ")
    if answer in quize:
        blank[quize.index(answer)]=answer
    print(blank)
    if (answer in quize) and not("'_'" in blank):
        print("성공입니다")
        break
finish=t.time()

nowtime=(finish-start)*1000
print(nowtime)

infile.close()







