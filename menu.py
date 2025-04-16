import tkinter as tk
from tkinter import messagebox

menu = {
    'pizza': 100,
    'salad': 150,
    'coffee': 140,
    'veggies': 160,
    'fries': 180
}

order_total = 0
selected_items = []

def add_to_order():
    global order_total
    item1 = entry_item1.get().lower()
    item2 = entry_item2.get().lower()
    
    items_to_check = [item1, item2]
    added = False

    for item in items_to_check:
        if item in menu:
            order_total += menu[item]
            selected_items.append(item)
            added = True
        else:
            messagebox.showwarning("Invalid item", f"'{item}' is not on the menu.")
            return
    
    if added:
        messagebox.showinfo("Item Added", f"Items added: {', '.join(items_to_check)}")
        label_total.config(text=f"Total: ${order_total}")
        entry_item1.delete(0, tk.END)
        entry_item2.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Menu Ordering System")
window.geometry("400x400")
window.configure(bg="#f9f9f9")

# Greeting
tk.Label(window, text="Greetings fellow customer!", font=("Helvetica", 14), bg="#f9f9f9").pack(pady=10)
tk.Label(window, text="Please choose something from the menu:", bg="#f9f9f9").pack()

# Menu Display
menu_text = "\n".join([f"{item}: ${price}" for item, price in menu.items()])
tk.Label(window, text=menu_text, font=("Courier", 12), bg="#f0f0f0", justify="left").pack(pady=10)

# Entry fields
entry_item1 = tk.Entry(window, width=30)
entry_item1.pack(pady=5)
entry_item1.insert(0, "Enter first item")

entry_item2 = tk.Entry(window, width=30)
entry_item2.pack(pady=5)
entry_item2.insert(0, "Enter second item")

# Order Button
tk.Button(window, text="Add to Order", command=add_to_order).pack(pady=15)

# Total Label
label_total = tk.Label(window, text="Total: $0", font=("Helvetica", 12), bg="#f9f9f9")
label_total.pack()

window.mainloop()
