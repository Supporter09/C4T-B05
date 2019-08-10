computer_price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000,
}
user_key = input("Type of computer you want to check: ")
print("Price of",user_key,":",computer_price[user_key.upper])
