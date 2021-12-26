numbers = 100
for number in range(numbers):
    if number % 7 == 0:
        continue
    elif "7" in str(number):
        continue
    print(number)

# the solution by teacher
for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):
        continue
    print(i)
