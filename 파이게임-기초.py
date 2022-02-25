import pygame as p

p.init() #pygame 초기화

size=[400,400] #[가로 크키,세로크기]

sc=p.display.set_mode(size) #해상도 설정(게임 창 크기 설정)

p.display.set_caption('파이게임 기초') #윈도우 창 제목 설정
red=(255,0,0)  #빛의 3원색(R,G,B)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
yellow=(255,255,0)
playing=True
while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 감지
        if event.type ==p.QUIT: #윈도우 x버튼 을 눌렀으면
            p.quit() #파이게임 프로그램 끄는 명령어
            quit() #결과창 끄는 명령어
            playing = False
    sc.fill(white) #배경 색 변화
    p.draw.polygon(sc,green,[[100,100],[300,100],[200,0]],0) #[꼭짓점좌표값], ,5=선두께 (0을 넣으면안쪽 색이 채워짐)
    p.draw.lines(sc,red,False,[[120,100],[120,200],[280,200],[280,100]],5)
    p.draw.lines(sc,black,False,[[160,140],[160,190],[240,190],[240,140],[160,140]],3)
    p.draw.lines(sc,black,False,[[200,140],[200,190],[200,165],[160,165],[240,165]],3)
    p.draw.circle(sc,red,[360,40],40)
    

    p.display.flip() #파이게임 화면 업데이트 
    
