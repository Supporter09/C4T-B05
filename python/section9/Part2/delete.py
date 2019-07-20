while True:
    color = ['red','yellow','blue','orange','pink']
    for i,color1 in enumerate(color):
        print(i,color1)

    user_delete = input("Items you want to delete : ")

    if user_delete.isdigit() :
        num = int(user_delete)
        color.pop(num)
        print("Our color list : ")
        for i,color1 in enumerate(color):
            print(i,color1)
        break
    elif user_delete.isalpha() :
        word = user_delete
        color.remove(word)
        print("Our color list : ")
        for i,color1 in enumerate(color):
            print(i,color1)
        break 
    else:
        print("Try again")
        break