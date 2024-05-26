import random 
print(" WELCOME TO THE WORLD OF ROCK,PAPER AND SCISSORS!!!","\n","ENTER 'r' FOR ROCK","\n","ENTER 'p' FOR PAPER","\n","ENTER 's' FOR SCISSORS","\n" ,"ENTER 'Z' TO STOP")
print("\n"," LETS PLAY!!!")
print("")
while True:
    random_choice=random.choice(["R","P","S"])
    a=input("Enter Your Weapon:").upper()
    if a==random_choice:
        print("IT'S A DRAW")
    elif a=="R":
        if random_choice=="S":
            print(" CONGRATS...YOU WON!!!")
        else:
            print("YOU LOST","TRY AGAIN")
    elif a=="P":
        if random_choice=="R":
            print("CONGRATS...YOU WON !!!")
        else:
            print("YOU LOST","TRY AGAIN")
    elif a=="S":
        if random_choice=="P":
            print("CONGRATS...YOU WON!!!")
        else:
            print("YOU LOST","TRY AGAIN")
    elif a=="":
        print("ENTER A WEAPON","\n","ENTER 'r' FOR ROCK","\n","ENTER 'p' FOR PAPER","\n","ENTER 's' FOR SCISSORS","\n" ,"ENTER 'Z' TO STOP")
    elif a=="Z":
        print("")
        print("**GAME OVER**")
        break
