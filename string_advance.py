#string_advance

#print(),input()[str],variable
#datatype[int,float,str,list...]
#op 산술,비교...

coffee='americano' #str
#내장함수:[print,input,int,float,str,list...]
#len():길이를 알려주는 기능
print(len(coffee))#9
print(coffee.upper())#AMERICANO
print(coffee.lower())#americano
print(coffee.capitalize())#Americano
print(coffee.strip())#( )amricano( )[공백 삭제]
print(coffee.find('c'))#몇번째에 'c'가 있니? 5 없으면 -1
print(coffee.replace('cano','can'))#old(왼쪽)에서 new(오른쪽)으로
print(coffee.count('a'))#a의 개수 2 없으면-1

a='mega'
b='study'
c=a+b #문자열 연결 연산자
d=a*3 #문자열 반복 연산자
e=a[0] #[]문자열 인덱싱 결과:m
f=b[0:3] #문자열 슬라이싱 dy제외 결과:stu
g='g'in a #mega에 g가 있니?

title="m p 3"
print(title.split())#공백 기준 str에서 list로
t1="orange,apple,banana"
print(t1.split(','))#,기준

#em=str(input("이메일 주소 입력:"))
#l=em.split('@')
#t=l[1].split('.')
#l[1]=t[0]
#l.append(t[1])
#print(l)

A='asdasd'

nA=A.replace('after','before').replace('it','🤣').split()
print(nA)

