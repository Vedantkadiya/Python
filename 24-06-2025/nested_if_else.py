n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))     
n3 = int(input("Enter the number 3: "))
if n1 > n2:
    if n1 > n3:
        print(n1, "is the largest number among 3")
    else:
        print(n3, "is the largest number among 3")
else:
    if n2 > n3:
        print(n2, "is the largest number among 3")
    else:
        print(n3, "is the largest number among 3")