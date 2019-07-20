color = ["orange","red","blue","green"]
print("Our color is :")
print(*color,sep=",")

user_color = input("Enter a new color : ")
print(user_color)
color.append(user_color)
print(*color,sep=", ")