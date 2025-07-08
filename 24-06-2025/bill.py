total = 0
print("Welcome to simple Billing System")
print("------ MENU ------")
print("1. Tea       -rs10")
print("2. coffee    -rs20")
print("3. samosa    -rs25")
print("4. Burger    -rs50")
print("5. Pizza     -rs150")
print("-------------------")
print("Enter 0 to finish and generate bill")

while True:
    choice = int(input("Enter Item Number: "))

    if choice == 0:
        break

    qty = int(input("Enter Quantity: "))

    if choice == 1:
        print(f"Added {qty} Teas(s)")
        total += 10 * qty
    elif choice == 2:
        print(f"Added {qty} Coffee(s)")
        total += 20 * qty
    elif choice == 3:
        print(f"Added {qty} Samosa(s)")
        total += 25 * qty
    elif choice == 4:
        print(f"Added {qty} Burger(s)")
        total += 50 * qty
    elif choice == 5:
        print(f"Added {qty} Pizza(s)")
        total += 150 * qty
    else:
        print("Invalid choice please select a valid item.")

gst = total * 0.18
grand_total = total + gst

print("\n----- FINAL BILL ------")
print(f"Subtotal: rs{total}")
print(f"GST(18%): RS{gst:.2f}")
print(f"Total Payable: ₹{grand_total:.2f}")
print("------------------------")
print("Thank you! Visit again.")