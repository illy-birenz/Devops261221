def sqre(x):  # this is the definition of the function, x is what the function will get
    print(x * x)


def mul(x, y):
    print(x * y)


x = 10
sqre(100)  # calling the function at top, will gve it 100 and will do 100 * 100
mul(100, 9)

###  the below an example that we have double code, since the below has same code, we can change the below

input_from_user = int(input("enter your age: "))
if input_from_user > 0:
    print("age is ok")

input_from_user = int(input("enter your number of pts: "))
if input_from_user > 0:
    print("number of pets is approved")


### the below is the new funtion created from the above
def check_input(gt, input_string, print_string):  # gt is greater than
    input_from_user = int(input(input_string))
    if input_from_user > gt:
        print(print_string)


check_input(0, "enter your age: ", "age is ok")


# the below is the new funtion created from the above
def check_input(gt, input_string):  # print_string no longer used, was greyed out and thus removed
    input_from_user = int(input(input_string))
    if input_from_user > gt:
        return True
    else:
        return False


result = check_input(0, "enter your age2: ")
if result == True:
    print("age is ok2")

result = check_input(0, "enter number of pets2: ")
if result == True:
    print("pets are approved2")
