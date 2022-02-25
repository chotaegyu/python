import pygame as p
p.init()
size=(500,500)
sc= p.display.set_mode(size)
p.display.set_caption("image_music")
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
yellow=(255,255,0)
#이미지를 변수에 넣기
d=p.image.load("Mine.png")
a=p.image.load("s.png")
b=p.image.load("sans1.png")
#음악 넣기
p.mixer.music.load("fight.mp3")
p.mixer.music.play(0) #-1은 무한 반복
p.mixer.music.stop() #노래 정지
playing=True
while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 감지
        if event.type ==p.QUIT: #윈도우 x버튼 을 눌렀으면
            p.quit() #파이게임 프로그램 끄는 명령어
            quit() #결과창 끄는 명령어
            playing = False
    sc.fill(white)
    sc.blit(d,[100,100])
    sc.blit(a,[200,300])
    sc.blit(b,[300,100])
    p.mixer.music.play(-1)
    p.display.flip() #파이게임 화면 업데이트
    





