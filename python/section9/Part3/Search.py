num_list = [ 2,55,66,-94,5,39,45]
def check_list():
    input_num = int(input("Enter a number: "))
    try:
        num_check=num_list.index(input_num)
    except ValueError:
        print("Not found in our list")
    else:
        print("found,position :",input_num)
check_list()