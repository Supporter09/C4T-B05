while True:
    print("___________CRUD SUMMARY___________")
    menu_list = ["C:creat","R:read","U:update","D:delete","Exit"]
    for i,menu_list in enumerate(menu_list):
        print(i,".",menu_list)
    print()
    user_input=int(input("Your choose: "))
    basic_list = ["HTML","Python","Java","JS","CSS"]
    if user_input == 0:
        user_fav = input("Enter your favorite things want to add:")
        basic_list.append(user_fav)
    elif user_input == 1:
        bl_len=len(basic_list)
        if bl_len == 0:
            print("there is nothing here ")
        else:
            for basic_list in basic_list:
                print(basic_list)
    elif user_input == 2:
        print(basic_list)
        user_place=int(input("Which place you want to update: "))
        update_thing = input("Thing you want to update: ")
        basic_list[user_place]=update_thing
    elif user_input == 3:
        print(basic_list)
        user_locate=int(input("Which place you want to delete: "))
        basic_list.pop(user_locate)
    elif user_input == 4:
        break
print(basic_list)

