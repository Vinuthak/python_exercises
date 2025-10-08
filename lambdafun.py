# with map()
numbers = [1,2,3,4,5]
result = map(lambda x: x*2 , numbers)
print(list(result))

# with sort()
numbers = [5,2,9,1]

numbers.sort(key = lambda n: n, reverse = True)
print(numbers)