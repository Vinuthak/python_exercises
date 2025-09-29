# Print each fruit on a new line.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Print each fruit with its index number (1, 2, 3 …).
for i, x in enumerate(fruits,start = 1):
    print(f"{i} - {x}")