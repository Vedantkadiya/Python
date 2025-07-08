"""
There are 3 types of conditional statements 

1. Normal if - else
2. ladder if - else
3. nested if - else 

"""
age = int(input("Enter the age: "))
if age > 100:
    print("please mention a proper age !!")
elif age >= 18:
    print("You Are Eligible for vote !!")
else:
    print("You are not Eligible for vote !!")