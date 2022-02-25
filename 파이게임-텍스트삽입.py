import pygame as p
p.init()
sc=p.display.set_mode([500,500])
p.display.set_caption('텍스트삽입')
font1=p.font.SysFont("malgungothic",20)#(글씨체,글씨크기)
text=font1.render("와샌즈",True,(0,0,0))#("쓸내용",굵기설정,글색깔-RGb)
a=0


playing= True


while playing:
  

    for event in p.event.get():
        if event.type ==p.QUIT:
            p.quit()
            quit()
            playing = False
    if event.type==p.KEYDOWN:
        if event.key==p.K_UP:
            a+=1
        if event.key==p.K_DOWN:
            a-=1
        if event.key==p.K_SPACE:
            a=0
            

    

    sc.fill([255,255,255])
    text=font1.render("점수:{}".format(a),True,(0,0,0))#("쓸내용",굵기설정,글색깔-RGb)
    sc.blit(text,[200,200])

    p.display.flip()
    


