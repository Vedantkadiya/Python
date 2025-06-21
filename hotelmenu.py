menu = {
    'Pizza':40,
    'Pasta':70,
    'Salad':50,
    'Tea':25,
    'Coffee':75,
}

print("Welcome to the Programming wala Resturant")
print("Pizza: rs40\nPasta: rs70\nSalad: rs50\nTea: rs25\nCoffee: rs75")

order_total = 0

item_1 = input("Enter the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to the order")
else:
    print(f"Ordered item {item_1} is not availabel yet")

another_order = print("Do you want to add another item? (Yes/No)")
item_2 = input("Enter the another item you want to order: ")
if another_order == "Yes":
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to the order")
else:
    print(f"Ordered item {item_2} is not availabel yet") # type: ignore
print(f"The total amount of item orer is:{order_total}")

    