def determine_the_number(n):
    if n == 0:
        print(f"{n} is Zero")
    elif n < 0:
        print(f"{n} is negative number")
    else:
        print(f"{n} is positive number")

n = int(input("Enter a number: "))

determine_the_number(n)