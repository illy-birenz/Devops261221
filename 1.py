print("hello")
my_var = 10
print(my_var)
my_name = "Illy"
print(my_name)
is_true = False
my_list = ["zero", "one", 31, True]
print(my_list[1])
my_dict = {"name": "illy",
           "lname": "biren",
           "age": "40",
           "is_married": "False"}
print(my_dict["name"])
print(my_dict.keys())
my_number = 5 * 2
my_other = 5 * "illy "  #string multiplied will print same value that number of times
print(my_other)

if my_number == 10:  #the ':' tells python it's a function and pycharm will automatically indent the next line
    print("my_number")
print(f"your result is {my_list[2:0:-1]}")  #run on list based on rules
print(f"your result is {my_list[4:0:-1]}")  #run on list based on rules