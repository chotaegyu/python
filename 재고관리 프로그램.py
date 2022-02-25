a=0
b=0
c=0
i={"메로나":300,'비비빅':400,'죠스바':250}
while True:
    print("1.재고확인")
    print("2.물품추가")
    print("3.재고삭제")
    print("4.재고수정")
    print("5.프로그램종료")
    a=int(input("실행할 항목 번호를 입력해주세요:"))
    if a==1:
          print(i)
    if a==2:
        b=input("추가할 품목을 입력해주세요:")
        c=int(input("품목의 재고를 입력해주세요:"))
        i[b]=c
        print("추가되었습니다")
    if a==3:
          b=input("삭제할 품목을 입력해주세요:")
          del i[b]
          print("삭제되었습니다")
    if a==4:
          b=input("수정할 품목을 입력해주세요:")
          c=int(input("품목의 재고값을 입력해주세요:"))
          i[b]=c
    if a==5:
            break
          
          
        
