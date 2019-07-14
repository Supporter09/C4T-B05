year = int(input("Year : "))
month = int(input("Month : "))

for i in range(1,8,2):
    if month == i:
        print("thang",month,"co 31 ngay.")

for i in range(4,7,2):
    if month == i:
        print("thang",month,"co 30 ngay.")

for i in range(8,13,2):
    if month == i:
        print("thang",month,"co 31 ngay.")

for i in range(9,11,2):
    if month == i:
        print("thang",month,"co 30 ngay.")
    

if year % 4 == 0:
    if month == 2 :
        print("thang",month,"co 28 ngay.")
elif year % 4 != 0:
    if month == 2:
        print("thang",month,"co 29 ngay")