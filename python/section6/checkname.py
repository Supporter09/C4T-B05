
while True:
    name = input("Nhap ten cua ban vao day :")
    if name.isalpha():
        print("Ten hop lệ")
        break
    else:
        print("Tên không hợp lệ")
        