
import pygame as p
p.init()
sc=p.display.set_mode([500,500])
p.display.set_caption('이미지 불러오기')
playing= True
i=p.image.load("sans1.png")
i2=p.image.load("Mine.png")
a=0
b=0
c=0
d=0

while playing:
    

    for event in p.event.get():
        if event.type ==p.QUIT:
            p.quit()
            quit()
            playing = False
    sc.fill([255,255,255])
    #sc.blit(i,[1,100]) #[x좌표,y좌표]
    a+=c
    b+=d
    if a>=400 and b<=0:
        c=0
        d=0.5
    if a<=0 and b<=0:
        c=0.5
        d=0
    if b>=400 and a>=400:
        c=-0.5
        d=0
    if a<=0 and b>=400:
        c=0
        d=-0.5
    
    sc.blit(i,[a,b])

    p.display.flip()
    


