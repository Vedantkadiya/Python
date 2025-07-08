name = input("Type Your Name: ")
print("welcome", name ,"to this adventure!")
answer = input(
    "You are on a dirt road , it has come to an end and you can go left or right. Which Way Would You Like To Go?  ").lower()

if answer == "left":
    answer = input("You come to a river , you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You Swam accross and were eaten by alligator")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You Lose")

elif answer == "right":
    answer = input("You come to a bridge , it lokks wobbly, do you want to cross it or head back ? (cross/back)  ").lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)").lower()


        if answer == "yes":
            print("You talk to the stranger and they give you gold.You win ! ")
        
        elif answer == "no":
            print("You ignore the stranger and they are offended You lose !")
        else:
            print("Not a valid option. You Lose")

    else:
        print("Not a valid option. You Lose")

else:
    print("Not a valid option. You Lose.")

print("Thank You For Trying !", name)



