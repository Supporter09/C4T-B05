from turtle import *

bankinh = int(input("Nhập bán kính của hình tròn : ")) 
vien = input("Nhập màu viền bạn thích : ")
fill = input("Nhập màu hình tròn bạn thích : ")

color(vien)
fillcolor(fill)

begin_fill()
circle(bankinh)
end_fill()

mainloop()