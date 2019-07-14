# while True:
# import random
# # # def freaken_game():
# num1 = random.randrange(100)
# num2 = random.randrange(100)
# sum2 = random.randrange(100)
# sum1 = num1 + num2
# print(num1,"+",num2,"=",sum2)

# userinput = input("Answer the question : ")
# point=0
# if userinput == sum1:
#     num1 = random.randrange(100)
#     num2 = random.randrange(100)
# print(num1)
# print(num2)
# print(sum1)
while True:
    def addition():
        num1 = random.randint(-100,100)
        num2 = random.randint(-100,100)
        num3 = random.randint(-1,1)
        sum1 = num1 + num2
        sum2 = sum1 + num3
        # print(num1)
        # print(num2)
        # print(sum2)

    import random
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    num3 = random.randint(-1,1)
    sum1 = num1 + num2
    sum2 = sum1 + num3
    print("O for true; X for false")
    print(num1,"+",num2,"=",sum2)
    userinput= input("Your answer: ")
    if userinput == "O":
        if sum1 == sum2:
             addition()
             print("True")
             print()
        elif sum1 != sum2:
             print("Game Over")
             break
    elif userinput == "X":
        if sum1 != sum2:
             addition()
             print("True")
             print()
        elif sum1 == sum2:
             print("Game Over")
             break

    
    



    def Subtraction():
        num1 = random.randint(-100,100)
        num2 = random.randint(-100,100)
        num3 = random.randint(-1,1)
        sub1 = num1 - num2
        sub2 = sub1 + num3
        # print(num1)
        # print(num2)
        # print(sub2)
        # print(num1,"-",num2,"=",sub2)

    def Multiplication():
        num1 = random.randint(-50,50)
        num2 = random.randint(-50,50)
        num3 = random.randint(-1,1)
        mult1 = num1 * num2
        mult2 = mult1 + num3
        print(num1)
        print(num2)
        print(mult2)
        print(num1,"x",num2,"=",mult2)

    def chia():
        num1 = random.randint(-50,50)
        num2 = random.randint(-50,50)
        num3 = random.randint(-1,1)
        chia1 = num1 / num2
        chia2 = chia1 + num3
        print(num1)
        print(num2)
        print(chia2)
        print(num1,":",num2,"=",chia2)



    # addition()
    # print()
    # Subtraction()
    # print()
    # Multiplication()
    # print()
    # chia()

