import tkinter as tk

def add_item():
    item = item_textbox.get()
    print(item)

window = tk.Tk()

item_textbox = tk.Entry(window)
item_textbox.pack()

add_button = tk.Button(
    window,
    text="Add Item",
    command=add_item
)
add_button.pack()

window.mainloop()