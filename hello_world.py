# print("Hello World")
# print("Enter your name")
# name = input()
# print("Hello " + name)
try:
    choice = int(input("Enter a number: "))
    print("You chose:", choice)
except ValueError:
    print("Not a number!")
      
