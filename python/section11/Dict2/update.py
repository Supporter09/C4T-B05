number_of_computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
user_key = input("Nhập loại sản phẩm mà bạn muốn thay đổi :")
user_amount = int(input("Số lg sản phẩm mới là : "))
number_of_computer[user_key.upper()]= user_amount

user_want = input("Sản phẩm bạn muốn kiểm tra là :")
print("Số lg",user_want,"còn trong kho là :",number_of_computer[user_want.upper()])
