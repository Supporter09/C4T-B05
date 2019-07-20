import random
array1= ["Orange","Apple","Banana","Melon"]

random_word = random.choice(array1)

random_list = list(random_word)

shuffle = random.sample(random_list,len(random_list))
print("Jumpled word:")
for i in shuffle:
    print(i)

user_input = input("Your answer : ")

if user_input == random_word:
    print("Your answer is correct!!")
elif user_input != random_word:
    print("<<Your answer is incorrect>>")

