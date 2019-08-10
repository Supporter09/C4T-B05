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
user_want = input("Type of computer you want to buy: ")
user_amount = int(input("Amount : "))
print("Your bill :",user_amount*computer_price[user_want.upper()],"$")
