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

user_want = input("Sản phẩm bạn muốn kiểm tra là :")
print("Số lg",user_want,"còn trong kho là :",number_of_computer[user_want.upper()])

user_key = input("Nhập loại sản phẩm mà bạn muốn thay đổi :")
user_amount = int(input("Số lg sản phẩm mới là : "))
number_of_computer[user_key.upper()]= user_amount

sum = 0
for value in number_of_computer.values():
    sum += value
print("Tổng số máy có trong kho là :",sum)

user_key_value = input("Nhập hãng máy và số lg đã xuất :")
key_value = user_key_value.split(":")

print("Lg máy",key_value[0].upper(),"còn lại trong kho là :", number_of_computer[key_value[0].upper()]-int(key_value[1]))

name_of_com = ["HP","DELL","MACBOOK","ASUS","TOSHIBA","FUJITSU","ALIENWARE"]
for i in name_of_com:
    print(number_of_computer[i]*computer_price[i])
