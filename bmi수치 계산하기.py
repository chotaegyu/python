a= int(input("키를 입력해주세요(cm단위):"))
b = int(input("몸무게를 입력해주세요(지구기준,kg기준):"))
c=b/(a/100)**2
print("bmi수치는",c,"로")
if c<20:
        print("저체중입니다")
elif c>=20 and c<= 24:
    print("정상입니다")
elif c>=25 and c<=29:
    print("과체중입니다")
elif c>=30:
    print("비만입니다")
