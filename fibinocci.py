first_number = 0
second_number = 1
# fibinocci = [first_number, second_number]

n = int(input("Enter a number to get its fibinocci sequence till that number: "))
if n == 0:
    print(first_number)
elif n == 1:
    print(first_number, second_number)
else:
    
    # while second_number < n:
        # second_number = first_number + second_number
        # first_number = second_number
        # fibinocci.append(first_number)
        # n = n - 1
    # print(fibinocci)
    for fibinocci in range(n):
        new_fib = first_number+second_number
        first_number = second_number
        second_number = new_fib
        print(new_fib)