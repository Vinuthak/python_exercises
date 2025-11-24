def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
    
print(is_leap(1990))




# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# # year = int(input())
# print(is_leap(2400))