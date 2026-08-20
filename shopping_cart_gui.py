import tkinter as tk

def add_item():
    item = item_textbox.get()
    amount = amount_textbox.get()

    if item == "" or amount == "":
        print("Please fill in both textboxes")
        return

    if amount.isalpha():
        print("Amount cannot contain letters")
        return

    print(item, amount)

        # Add item and amount to the Listbox
    item_listbox.insert(tk.END, f"{item:<15} {amount}")

    # Clear the textboxes
    item_textbox.delete(0, tk.END)
    amount_textbox.delete(0, tk.END)

def add_amount():
    amount = amount_textbox.get()
    print("Amount:", amount)

def sort_items():
    items = list(item_listbox.get(0, tk.END))

    # Sort alphabetically by the item name
    items.sort(key=lambda x: x.split()[0].lower())

    # Remove existing items
    item_listbox.delete(0, tk.END)

    # Add sorted items back
    for item in items:
        item_listbox.insert(tk.END, item)


window = tk.Tk()
window.title("Shopping Cart")

# Row 1: Item
item_label = tk.Label(window, text="Insert name")
item_label.grid(row=0, column=0, padx=10, pady=10)

item_textbox = tk.Entry(window)
item_textbox.grid(row=0, column=1, padx=20, pady=10)

# Row 2: Amount
amount_label = tk.Label(window, text="Insert amount")
amount_label.grid(row=1, column=0, padx=10, pady=10)

amount_textbox = tk.Entry(window)
amount_textbox.grid(row=1, column=1, padx=20, pady=10)

add_button = tk.Button(
    window,
    text="Add Item",
    command=add_item
)
add_button.grid(row=1, column=2, padx=20, pady=10)

# Row 3:Listbox
item_listbox = tk.Listbox(window, width=30)
item_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Row 4: Sort Button
sort_button = tk.Button(
    window,
    text="Sort Alphabetically",
    command=sort_items
)

sort_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)


window.mainloop()