import random
item_list = ["Rock" , "Paper" , "scissor"]

user_choice = input("Enter your move : Rock ,Paper,scissor =")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses the same hence it is a tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("paper covers rock hence computer win")
    else:
        print("Rock smashes scissor hence you win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("paper covers rock hence you win")
    else:
        print("scissor cuts the paper hence computer win")

elif user_choice == "scissor":
    if comp_choice == "Rock":
        print("rock smashes scissor hence computer wins")
    else:
        print("scissor cuts the paper hence you win")