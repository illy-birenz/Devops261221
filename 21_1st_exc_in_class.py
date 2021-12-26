is_true = False
a = 2
b = 2.5
str_one = "One"
str_three = "Three"

if a > 2 and str_one == "One" or not str_three == "two":
    print("a is greater than 2")
elif b == 2.5:
    print("something")
elif str_one == "3":
    print("bla")
else:
    print("a is lower then 2")

my_list = ["hen", "lior", "shay", "ariel"]
my_other_list=["roni"]
if a > 0 and a <= 4:  # 0 < a <=4
    print("ok")

if my_list[0] == "hen" or \
        my_list[1] == "hen" or \
        my_list[2] == "hen" or \
        my_list[3] == "hen":
    print("hen is in my list")

if "hen" in my_list:
    print("we have found hen!")

if my_other_list:
    print("ther's conetnt in my_other_list, hello")

if len(my_list) > 0:
    print("my_list is bigger than zero,hey")

c = 5
d = 5
if c is d:
    print("c is d")

e = ["aaa"]
f = ["aaa"]
if e is f:
    print("e is f")

g = ["aaa", "1"]
h = ["aaa", "1"]
i = 9
if g is h:
    print("g is h")

if type(i) is int: # relevant to check whther a result we got bck from external code is indeed the type we expected
    print("i is an integer")

