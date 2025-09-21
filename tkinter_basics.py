import tkinter as tk
# create the main window
window = tk.Tk()
window.title("My Restaurant Menu: ")
window.geometry("1200x1200")   

# create a string variable to associate with the label

text_var = tk.StringVar()
text_var.set("Choose your menu:")

# create the label widget with all options
label = tk.Label(window,
                    textvariable = text_var,
                    anchor = tk.N,
                    bg = "lightgreen",
                    height = 3,
                    width = 30,
                    bd = 3,
                    font = ("Arial", 16, "bold"),
                    cursor = "hand2",
                    fg = "red",
                    padx=15,               
                    pady=15,                
                    justify=tk.CENTER,    
                    relief=tk.RAISED,     
                    underline=0,           
                    wraplength=250   )
# pack the label into the window
label.pack(pady=20) # Add some padding to the top

# Run the main event loop
window.mainloop()