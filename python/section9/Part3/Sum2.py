user_list = input("Enter a list of numbers, separated by ‘ ‘: ")
user_list2= user_list.split()
sum1=0
for i in user_list2:
    num = int(i)
    sum1 += num
print("Sum of all entered numbers:",sum1)