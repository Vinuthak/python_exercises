menu = [
    ("Pizza", 8.5),
    ("Burger", 6.0),
    ("Salad", 5.5),
    ("Pasta", 7.5),
    ("Juice", 3.0)
] #each menu item is a tuple(dish_name,price)
order = [] #stores orders
print("\n Restaurant Ordering System")

def show_menu():
    print("\n-- Menu --")
    for i, (dish_name,price) in enumerate(menu,start=1):
        print(f"{i} . {dish_name} - {price:.2f}")

def show_order():
    if not order:
        print("\n your order is empty")
    else:
        print("\n --Your order--")
        total = 0
        for i,(dish_name,price) in enumerate(order,start=1):
            print(f"{i}.{dish_name} - ${price:.2f}")
            total += price
        print(f"Total: ${total:.2f}")

while True:

    print("\n--- Restaurant Ordering System ---")
    print("1. View Menu")
    print("2. Add Item to Order")
    print("3. View Order")
    print("4. Remove Item from Order")
    print("5. Checkout & Exit")
    

    choice = input("Choose an option: ")
    
    if choice == "1":
        show_menu()
    elif choice == "2":
        try:
            show_menu()
            item_number = int(input("Enter an item number to add : "))
            if 1 <= item_number <= len(menu):
                order.append(menu[item_number-1])
                # print(f"Added {menu[item_number-1]}") this code gives ("pizza", 8.50) since we wanted to print only item without price we go into the tuple with the following code
                print(f"Added {menu[item_number-1][0]}")
            else:
                print("Invalid number.")   

        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        show_order()
    
    elif choice == "4":
        show_order()
        if not order:
            print("Please add an item before removing")
            show_menu()
        else:
            try:
                remove_number = int(input("Enter item number to remove: "))
                if 1 <= remove_number <= len(order):
                    removed = order.pop(remove_number-1)
                    print(f"{removed[0]} is removed from your order.")
                    show_order()
                    
            except ValueError:
                print("Invalid number")

    elif choice == "5":
        print("Thanks for visiting!")
        break
    else:
        print("Enter a valid number")


