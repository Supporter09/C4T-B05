number_of_computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
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