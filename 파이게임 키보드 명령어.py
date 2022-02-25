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
p.mixer.music.load("fight.mp3")
p.mixer.music.play(-1)
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
                sc.fill([255,0,0])
                c=0
                d=-50
                a+=c
                b+=d
            if event.key==p.K_DOWN:
                sc.fill([0,0,255])
                c=0
                d=50
                a+=c
                b+=d
            if event.key==p.K_LEFT:
                sc.fill([0,0,0])
                c=-50
                d=0
                a+=c
                b+=d
            if event.key==p.K_RIGHT:
                sc.fill([0,0,0])
                c=50
                d=0
                a+=c
                b+=d
        if event.type==p.KEYUP:
            if event.key==p.K_SPACE:
                p.mixer.music.play(-1)
            if event.key==p.K_UP:
                sc.fill([255,255,255])
            if event.key==p.K_DOWN:
                sc.fill([255,255,255])
            if event.key==p.K_LEFT:
                sc.fill([255,255,255])
            if event.key==p.K_RIGHT:
                sc.fill([255,255,255])
            
            

            
        sc.blit(i,[a,b])
    

    
    p.display.flip()
    
    


