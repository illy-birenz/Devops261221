fname = "illy"
lname = "biren"
print("hello " + fname + " " + lname)  #this is the most memory intense as it replicates the variable
print(f"hello {fname} {lname}") #f tells it to be a special string, inside the '{}' there will be a variable
# only from python 3.6 or so. aviel thinks it's the most readable
print("hello %s %s" % (fname, lname)) #define a string, variables are the %s and hen give me a list of variables to use

my_number = "4"
result = int(my_number) - 2  #convert string to int
print(result)
result = float(my_number) - 2  #converting to float
print(result)
print('your "result" is ' + str(result))  #converting to string, else it fails cause it computs the string and fails with adding string to float
print("hello", result)  #here the print gets two variables and prints them, not the same as above
print(f"your result is {result -2}")  #it works cause you tell python it's a sophisticated string




