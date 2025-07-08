"""
operator 
and : must be true all condition
or : any one condition
""" # type: ignore
n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))     
n3 = int(input("Enter the number 3: "))

if n1>n2 and n1>n3:
    print(n1,"Is greatest")
elif n2>n1 and n2>n3:
    print(n2,"Is greatest ")
else:
    print(n3,"Is greatest ")