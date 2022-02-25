print("1.아메리카노 3000원")
print("2.카페라떼 2700원")
print("3.핫초코 2300원")
a = int(input("커피의 종류를 선택해주세요:(예:1)"))
b = int(input("몇잔을 드릴까요?"))
if a==1:
    
    a=3000
elif a==2:
    a=2700
elif a==3:
    a=2300
c= a*b
print("총금액은",c,"원입니다." )
d=int(input("돈을 투입해주세요:"))
print(d,"원을 받았습니다")
if d<c:
    print("돈이 모자랍니다")
elif d>c:
    print("거스름돈은",d-c,"원입니다")
