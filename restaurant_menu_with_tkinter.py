import tkinter as tk
from tkinter import messagebox

# Menu (dish: price)
menu = {
    "Pizza": 8.5,
    "Burger": 6.0,
    "Salad": 5.5,
    "Pasta": 7.5,
    "Juice": 3.0
}

root = tk.Tk()
root.title("Restaurant Menu")
root.geometry("300x350")

# Heading
label = tk.Label(root, text="🍴 Welcome to My Restaurant 🍴", font=("Arial", 12, "bold"))
label.pack(pady=10)

# Dictionary to store checkbox variables
vars = {}

# Create a checkbox for each dish
for dish, price in menu.items():
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=f"{dish} - ${price:.2f}", variable=var)
    chk.pack(anchor="w", padx=20)
    vars[dish] = (var, price)  # save variable + price

# Function to calculate bill
def show_bill():
    total = 0
    items = []
    for dish, (var, price) in vars.items():
        if var.get():  # if checked
            total += price
            items.append(dish)
    if items:
        messagebox.showinfo("Your Order", f"You ordered: {', '.join(items)}\nTotal: ${total:.2f}")
    else:
        messagebox.showwarning("Empty Order", "Please select at least one item.")

# Button to confirm order
btn = tk.Button(root, text="Place Order", command=show_bill)
btn.pack(pady=20)

root.mainloop()
