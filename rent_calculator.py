rent = int(input("Enter the rent of the house/flat :"))
food = int(input("Enter the amount of food oredered :"))
electricity_spend = int(input("Enter the total of electricity spend :"))
charge = int(input("The charge per unit if electricity:"))
persons = int(input("Enter the number of persons living in the flat/house:"))

total_bill = electricity_spend * charge
output = (rent + food + total_bill) // persons

print("each person will pay rent :",output)