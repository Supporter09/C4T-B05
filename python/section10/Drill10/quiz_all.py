question = ["Năm 2009, sau sự thành công của Ironman, hãng Disney đã mua lại Marvel với giá 4 tỷ USD vào năm nào?", "Trong Ironman, tổ chức nào đã bắt cóc Tony Stark ?"]  
answer = [["1.2007","2.2008","3.2009","4.2010"],["TEN RINGS","H.Y.D.R.A","S.H.I.E.L.D"]]
right_answer =["3.2009","TEN RINGS"]


count=0

print("MENU :")
print("1.Play")
print("2.EXIT")

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 2 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def print_question(count):
    print(question[count])
    answers = answer[count]
    for i in answers:
        print(i)

def check_answer(user_answer,count):
    if user_answer == right_answer[count]:
        count = count + 1
        print("Correct.")
        return count
    elif user_answer != right_answer[count]:
        print("Incorrect.")
        return count

def menu_option(user_choice, count):
    if user_choice == 1:
        print_question(count)
        user_answer =input("Câu trả lời của bạn (Xin đánh đầy đủ câu trả lời):")
        check_answer(user_answer,count)
        count = check_answer(user_answer,count)
        return count
def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep = "")


def main():
    option = get_user_input()
    total = 0
    correct = 0
    while option != 2:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()
        while total == 2:
            break
    # while option == 2:
    print("Exit the quiz.")
    display_result(total, correct)
    # break

main()




