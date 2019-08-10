number_of_computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
number_of_computer["TOSHIBA"]= 10
user_want = input("Sản phẩm bạn muốn kiểm tra là :")

print("Số lg",user_want,"còn trong kho là :",number_of_computer[user_want.upper()])
