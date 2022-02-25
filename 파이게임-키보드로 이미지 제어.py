import pygame as p

p.init()
sc=p.display.set_mode([500,500])
p.display.set_caption('키보드 조작')
playing= True
i=p.image.load("sans1.png")

a=200
b=200
c=0
d=0
while playing:
    
    for event in p.event.get():
        if event.type ==p.QUIT:
            p.quit()
            quit()
            playing = False
            
    if event.type ==p.KEYDOWN:#키보드를 눌렀을때
        if event.key==p.K_SPACE:
            p.mixer.music.stop()
        if event.key==p.K_UP:
            d=-1
        if event.key==p.K_DOWN:
            d=1
        if event.key==p.K_LEFT:
            c=-1
        if event.key==p.K_RIGHT:
            c=1
    if event.type == p.KEYUP:
        if event.key==p.K_UP or event.key==p.K_DOWN or event.key==p.K_RIGHT or event.key==p.K_LEFT:
            c=0
            d=0
    sc.fill([255,255,255])
    sc.blit(i,[a,b])
    a= a+c
    b= b+d
    p.display.flip()
