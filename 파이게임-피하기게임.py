import pygame as p
import random as r
p.init()
sc=p.display.set_mode([1000,500])
p.display.set_caption('피하기게임')
a=p.image.load("h.png")
b=a.get_rect(left = 0,top=0)
c=p.image.load("l.png")
d=c.get_rect(left = 900,top=400)
e=p.image.load("sp.png")
font1=p.font.SysFont("malgungothic",20)
font2=p.font.SysFont("malgungothic",100)
playing= True

g=0
h=5
while playing:

    for event in p.event.get():
        if event.type ==p.QUIT:
            p.quit()
            quit()
            playing = False
    if event.type ==p.KEYDOWN:
        if event.key ==p.K_UP:
            b.top -=5
        if event.key == p.K_DOWN:
            b.top +=5
    if b.top<=0:
        b.top+=5
    if b.top>=420:
        b.top-=5


    sc.fill([255,255,255])
    sc.blit(e,[0,0])
    d.left -=20
    if d.left<=0:
        d.left = 900
        d.top=r.randint(0,400)
        g+=1
    sc.blit(a,b)
    
    sc.blit(c,d)
    text1=font1.render("점수:{}".format(g),True,(255,255,0))
    text2=font1.render("목숨:{}".format(h),True,(255,255,0))
    text3=font2.render("Clear",True,(0,255,0))
    text4=font2.render("Game Over",True,(255,0,0))

    if b.colliderect(d):
        h-=1
        d.left = 900
    if h<=0:
        sc.blit(text4,[450,200])
        playing=False
    if g>=10:
        sc.blit(text3,[400,150])
        playing=False
    sc.blit(text1,[0,0])
    sc.blit(text2,[900,0])
    

    p.display.flip()
    


