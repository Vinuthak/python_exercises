number = int(input("Enter a number to get its factorial: "))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*i
print(factorial)