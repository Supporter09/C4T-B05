while True:
    password = input("Enter your password :")
    chieudai = len(password)
    print(chieudai)
   
    if password.isalpha():
        print("pass word thiếu chữ số.Vui lòng nhập lại")
    else:
        print("password hợp lệ")
        break
