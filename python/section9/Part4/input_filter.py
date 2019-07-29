num_input = input("Enter a list of numbers, separated by ‘,’: ")
num_input1 = num_input.split(',')
print(num_input1)
for i in num_input1:
    num = int(i)
    if num % 2 == 0:
        print(num)