#무작위 방향이동 
import turtle as t
import random as r

t_shape = ["classic","circle","turtle"]
t.speed(0)

#a = r.randint(1,360)
#print(a)
t.shape(t_shape[1])
for x in range(10000):
    a = r.randint(1,360)
    b = r.randint(1,20)
    t.setheading(a)
    t.forward(b)




