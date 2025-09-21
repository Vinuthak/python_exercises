from tkinter import *
window = Tk()
window.title("ToDo List")
window.geometry("420x420")
label = Label(window,text = "Second")
label2 = Label(window,text = "first")
label.pack()
label2.pack()
window.mainloop()
tasks = []










tasks.append("Duolingo")
tasks.append("Chanting")
tasks.append("Groceries")
print("Your tasks: ", tasks)

tasks.remove("Groceries")
print("Remaining tasks: " , tasks)
tasks.pop()
if not tasks:
    print("The list is empty")