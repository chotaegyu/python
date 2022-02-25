a = int(input("출생년도를 입력해주세요:"))
a = a%10
if a== 1 or a== 6:
    print("월요일에 신청 가능합니다")
elif a==2 or a==7:
    print("화요일에 신청 가능합니다")
elif a==3 or a==8:
    print("수요일에 신청 가능합니다")
elif a==4 or a==9:
    print("목요일에 신청 가능합니다")
elif a==5 or a==0:
    print("금요일에 신청 가능합니다")
