while True:
    username = input("Your username : ")
    password = input("Your password : ")
    email = input("Your email : ")
    checkpass = input("Rewirte your password : ")

    passlen = len(password)
    if passlen > 8:
        print("Mật khẩu hợp lệ")
        if password == checkpass :
            print("Password check!")
            break
        else:
            print("please try again")
    else:
        print("Mật khẩu của bạn chưa đủ 8 kí tự ")