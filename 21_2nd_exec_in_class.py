print("hello world!")
print("hello world!")
print("hello world!")
print("hello world!")

what_to_print = "hello world!\n"
print(what_to_print * 4)

print(list(range(5)))
print(list(range(9, 2, -1)))
# enhancing the print we did above
for i in (range(4)):
    print(what_to_print)
# enhancing over the above
number_of_prints = 4
for i in (range(number_of_prints)):
    print(what_to_print)
# enhancing the above again with specific range and print of numbers
for i in range(1, number_of_prints):
    print(str(i) + ") " + what_to_print)

list_of_names = ["michael", "noam", "lior", "amichai"]
for i in range(len(list_of_names)):  # the loop here work according to the index which is the i
    print(list_of_names[i])

for name in list_of_names:  # the same as the above but with for each
    print(name)
    # can pull the index with (list_of_names.index(name))

a = 0
while a < 10:
    print(a)
    a = a + 1

for name in list_of_names:
    if name == "hen":
        break  # will stop the loop at this instant

for name in list_of_names:
    if name == "hen":
        continue  # continue means that once this part exists in the loop, it will ignore rest of lines in loop and start it again with next index
    print(name)

a = 0
while a < 10:
    print(a)
    a = a + 1
else:
    print("finished successfully")

a = "a"
while a != "q":
    a = input("enter q or not: ")
else:
    print("adas")