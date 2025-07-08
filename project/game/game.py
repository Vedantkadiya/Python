print ("Welcome to my computer quiz")

playing = input("Do You Want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play :)")

answer = input("What Does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
else:
    print("incorrect !")


answer = input("What Does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
else:
    print("incorrect !")
    

answer = input("What Does RAM  stands for? ")
if answer.lower() == "Random access memory ":
    print('Correct!')
else:
    print("incorrect !")
    

answer = input("What Does PSU stands for? ")
if answer.lower() == "power supply":
    print('Correct!')
else:
    print("incorrect !")
    
    
