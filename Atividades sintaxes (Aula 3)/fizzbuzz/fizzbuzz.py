num = 1
for i in range (0,30):

    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} Fizzbuzz")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
    num += 1
