my_dict = {"fname": "illy",
           "lname": "biren",
           "age": 40,
           "is_married": False}
# print(my_dict)
key_to_print = input(f"enter key from the following list: {list(my_dict.keys())}\n")  #input is always as string
# on the above we convert to list in order to remove the 'my_dict[' from the actual text
print("you chose to print " + str(my_dict[key_to_print]))
