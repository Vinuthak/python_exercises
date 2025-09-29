user_input = input("Enter a number, two numbers (comma separated), or a list: ")

#step1: Preprocess input
if user_input.startswith("[") and user_input.endswith("]"):
    values = user_input[1:-1].split(",")
else:
    values = user_input.split(",")

#convert to integers
values = [ int(v.strip()) for v in values if v.strip()]

# step2: match the shape
match values:
    case [x]:
        print(f"single number:  {x}")
    case [x,y]:
        print(f"two numbers: x is {x} and y is {y}")
    case [x, y, *rest]:
        print(f"A list of {len(values)} numbers: {values}")
    case _:
        print("invalid input")
