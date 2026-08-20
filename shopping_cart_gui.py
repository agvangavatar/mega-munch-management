import tkinter as tk

root = tk.Tk()
root.title("Mega Munch Management")

button_frame = tk.Frame(root)
button_frame.pack(padx=20, pady=20)

images = {
    "Apple": tk.PhotoImage(file="images/apple.png"),
    "Banana": tk.PhotoImage(file="images/banana.png"),
    "Carrot": tk.PhotoImage(file="images/carrot.png"),
    "Corn": tk.PhotoImage(file="images/corn.png"),
    "Tomato": tk.PhotoImage(file="images/tomato.png"),
    "Grapes": tk.PhotoImage(file="images/grapes.png"),
    "Orange": tk.PhotoImage(file="images/orange.png"),
    "Raspberry": tk.PhotoImage(file="images/raspberry.png"),
    "Broccoli": tk.PhotoImage(file="images/broccoli.png"),
    "Kiwi": tk.PhotoImage(file="images/kiwi.png"),
    "Melon": tk.PhotoImage(file="images/melon.png"),
    "Walnuts": tk.PhotoImage(file="images/walnuts.png"),
    "Flour": tk.PhotoImage(file="images/flour.png"),
    "Eggs": tk.PhotoImage(file="images/eggs.png"),
    "Butter": tk.PhotoImage(file="images/butter.png"),
    "Pie Crust": tk.PhotoImage(file="images/pie_crust.png"),
    "Cream Custard": tk.PhotoImage(file="images/cream_custard.png"),
    "Spinach": tk.PhotoImage(file="images/spinach.png"),
    "Parmesan": tk.PhotoImage(file="images/parmesan.png"),
    "Milk": tk.PhotoImage(file="images/milk.png"),
    "Onion": tk.PhotoImage(file="images/onion.png"),
    "Bread Crumbs": tk.PhotoImage(file="images/bread_crumbs.png"),
    "Whipped Creme": tk.PhotoImage(file="images/whipped_creme.png"),
    "Granola Topping": tk.PhotoImage(file="images/granola_topping.png"),
    "Yogurt": tk.PhotoImage(file="images/yogurt.png"),
    "Pear": tk.PhotoImage(file="images/pear.png"),
    "Avocado": tk.PhotoImage(file="images/avocado.png"),
}

for index, (name, image) in enumerate(images.items()):
    row = index // 6
    column = index % 6

    tk.Button(
        button_frame,
        image=image,
        text=name,
        compound="top",
        width=100,
        height=110
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

root.mainloop()