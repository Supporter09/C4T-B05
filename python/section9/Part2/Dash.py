from turtle import *
color1 = ['red','yellow','blue','orange','pink']
i = 0
for x in range(len(color1)):
    color(color1[i])
    forward(100)
    i +=1


mainloop()