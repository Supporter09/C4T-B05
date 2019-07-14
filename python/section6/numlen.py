while True:
    number = input(" Enter the number :")
    numlen = len(number)

    if number.isalpha():
        print("Ban phai nhap chu so")
    else:
        print("So chu so la :",numlen)
        break

