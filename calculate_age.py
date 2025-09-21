from datetime import date

age = int(input("Enter your current age: "))
if age <= 0:
    print("You are not born yet!")
    quit()

future_age_input = int(input("Enter a number to know in which year you turn to that age: "))
currentyear = date.today().year
future_age_year = (future_age_input - age ) + currentyear
print("You will turn ", future_age_input ,"in " , future_age_year) 