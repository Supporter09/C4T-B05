import random
user_input=input("Enter a word : ")
user_input_list = list(user_input)
print(user_input_list)
input_shuffle = random.sample(user_input_list,len(user_input_list))
print("Jumpled word:")
for i in input_shuffle:
    print(i.upper())


