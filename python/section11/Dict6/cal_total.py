number_of_computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

computer_price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000,
}

number_of_computer["TOSHIBA"]= 10
number_of_computer["HP"]= 30
number_of_computer["MACBOOk"]= 2
number_of_computer["FUJITSU"]= 15
number_of_computer["ALIENWARE"]= 5
print(number_of_computer)

name_of_com = ["HP","DELL","MACBOOK","ASUS","TOSHIBA","FUJITSU","ALIENWARE"]
prices = []
for i in name_of_com:
    price=number_of_computer[i]*computer_price[i]
    print(i,":",price,"$")
    prices.append(price)

total = 0
for p in prices:
    total+=p
print("Tổng giá trị toàn bộ các máy trong kho là:",total,"$")
