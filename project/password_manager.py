pwd = input("What is the master password? ")

def view():
    with open('password.txt','a') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")

    


def add():
    name = input("Account name : ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n" )


while True:
    mode = input("would you like to add a new password or view existing one (view ,add), press q to quit?  ").lower()
    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue

