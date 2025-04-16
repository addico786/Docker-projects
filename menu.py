menu = {
    'pizza': 100,
    'salad': 150,
    'coffee': 140,
    'veggies': 160,
    'fries': 180
}

print("Greetings, fellow customer! Please choose something from the menu:\n")

# Display the menu
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price}")

order_total = 0

# Keep taking orders until valid item is chosen
while True:
    item_1 = input("\nEnter the name of the item you want to order: ").lower()
    item_2 = input("Enter the second item you want to order: ").lower()

    valid = False

    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item '{item_1}' has been added to the basket.")
        valid = True
    else:
        print(f"'{item_1}' is not on the menu. Try again.")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to the basket.")
        valid = True
    else:
        print(f"'{item_2}' is not on the menu. Try again.")

    if valid:
        break

print(f"\nYour total is: ${order_total}")

