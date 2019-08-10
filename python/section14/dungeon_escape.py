import random
array = [ ["  -  ","  -  ","  K  ", "  -  " ], ["  P  ","  -  ","  -  ", "  -  " ], ["  -  ","  E  ","  -  ", "  -  " ], ["  -  ","  -  ","  -  ", "  -  " ]]

print("Đây là game Dungeon escape")
print("Hướng dẫn:")
print("W,A,S,D để di chuyển cách thức di chuyển thì như các trò chơi khác")
print("X để thoát game hoặc đơn giản là thắng là ok thui")
random.shuffle(array)


print(array[0][0],array[0][1],array[0][2],array[0][3])
print(array[1][0],array[1][1],array[1][2],array[1][3])
print(array[2][0],array[2][1],array[2][2],array[2][3])
print(array[3][0],array[3][1],array[3][2],array[3][3])

key = array.index(["  -  ","  -  ","  K  ", "  -  " ])
player = array.index(["  P  ","  -  ","  -  ", "  -  " ])
exit1 = array.index(["  -  ","  E  ","  -  ", "  -  " ])
none = array.index(["  -  ","  -  ","  -  ", "  -  " ])


key_array = array[key]
player_array = array[player]
exit_array = array[exit1]
none_array = array[none]

key_found = key_array.index("  K  ")
player_found = player_array.index("  P  ")
exit_found = exit_array.index("  E  ")



def get_user_input():#Lấy lựa chọn người dùng#
    user_input = input("Your move ? ")
    while user_input != "W" and user_input != "A" and user_input != "S" and user_input != "D":
        print("Sorry I don't understand!")
        user_input = input("Please try again: ")
    else:
        return user_input

def print1():#In bản đồ#
    print(array[0][0],array[0][1],array[0][2],array[0][3])
    print(array[1][0],array[1][1],array[1][2],array[1][3])
    print(array[2][0],array[2][1],array[2][2],array[2][3])
    print(array[3][0],array[3][1],array[3][2],array[3][3])



def check_key(count): #Kiểm tra xem người chơi lấy được chìa khóa chưa#
    if array[key].count("  P  ") == 1:
        player_location = key_array.index("  P  ")
        if player_location == key_found:
            count += 1
            print("Player! You have a key. Now get to the Exit!")
            return count
        else:
            return count

def can_i_exit(answer):
    if array[exit1].count("  P  ") == 1:
        player_location2 = exit_array.index("  P  ")
        if player_location2 == exit_found:
            print("Wait!!! Let me check if you have a key!")
            if answer == 1:
                print("Ok! U can go out!  Have a nice day!")
            elif answer == 0:
                print("No! Please take the key first!")

def choose_W():
    new_array[player][player_found] = "  -  "
    new_array[player-1][player_found] = "  P  "
def option(array,user_input,count):
    new_array = []
    if user_input == "W":
        array[player][player_found] = "  -  "
        array[player-1][player_found] = "  P  " 
        print1()
        count =check_key(count)
        can_i_exit(count)
        return new_array
    elif user_input == "A":
        array[player][player_found] = "  -  "
        array[player][player_found-1]= "  P  "
        print1()
        count =check_key(count)
        can_i_exit(count)
        return new_array
    elif user_input == "S":
        array[player][player_found] = "  -  "
        array[player+1][player_found] = "  P  "
        print1()
        count =check_key(count)
        can_i_exit(count)
        return new_array
    elif user_input == "D":
        array[player][player_found] = "  -  "
        array[player][player_found+1] = "  P  "
        print1()
        count =check_key(count)
        can_i_exit(count)
        return new_array


count =0
option1 = option(get_user_input(),count)
while option1 != "X":
    option(get_user_input(),count)
    option1 = get_user_input()