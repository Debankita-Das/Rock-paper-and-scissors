import random
score=0
x='home'
options=['rock','paper','scissors']
print("Welcome to Rock, paper, scissors game!")
while x.lower()=='home':
    print("Game Menu:")
    print("1. Start \n2. How to play \n3. Exit")
    a=eval(input("Enter your choice:"))
    if a==3 or a=='3':
        print("Thanks for playing!")
        print("Final score:",score)
        break
    elif a==2 or a=='2':
        print("Game Instructions:")
        print("The classic rock-paper-scissors game! In this game the user chooses to play either rock or paper or scissors. \
The computer randomly chooses one from the three options. The player earns 1 point on winning, loses 1 on losing and doesn't earn or lose anything \
if it's a tie.")
        print("1. If the player chooses rock they will win if the computer chooses scissors and loose if computer chooses paper.")
        print("2. If the player chooses paper they will win if the computer chooses rock and loose if the computer chooses scissors.")
        print("3. If the player chooses scissors they will win if the computer chooses paper and loose if the computer chooses rock.")
        print("4. If both the player and the computer choose the same thing then it's a tie.")
        i=input("Press enter when you want to proceed.")
    elif a==1 or a=='1':
        while True:
            uinput=str(input("Enter what you wanna play, rock, paper or scissors? "))
            cinput=random.choice(options)
            if uinput.lower()=="rock":
                if cinput=="rock":
                    print("You: rock","Computer: rock","Result: A Tie!",sep="\n")
                    print("Score:",score)
                elif cinput=="paper":
                    print("You: rock","Computer: paper","Result: Aaaww. You lose! :(",sep="\n")
                    score-=1
                    print("Score:",score)
                else:
                    print("You: rock","Computer: scissors","Result: Good job! YOU WIN!:D",sep="\n")
                    score+=1
                    print("Score:",score)
            elif uinput.lower()=="paper":
                if cinput=="paper":
                    print("You: paper","Computer: paper","Result: A Tie!",sep="\n")
                    print("Score:",score)
                elif cinput=="scissors":
                    print("You: paper","Computer: scissors","Result: Aaaww. You lose! :(",sep="\n")
                    score-=1
                    print("Score:",score)
                else:
                    print("You: paper","Computer: rock","Result: Good job! YOU WIN!:D",sep="\n")
                    score+=1
                    print("Score:",score)
            elif uinput.lower()=="scissors":
                if cinput=="scissors":
                    print("You: scissors","Computer: scissors","Result: A Tie!",sep="\n")
                    print("Score:",score)
                elif cinput=="rock":
                    print("You: scissors","Computer: rock","Result: Aaaww. You lose! :(",sep="\n")
                    score-=1
                    print("Score:",score)
                else:
                    print("You: scissors","Computer: paper","Result: Good job! YOU WIN!:D",sep="\n")
                    score+=1
                    print("Score:",score)
            else:
                print("Invalid input! Try again!")
            print()
            print("Would you like to play again?")
            x=str(input("Enter 'y' to play again, 'n' to exit the game or 'home' to return to main menu:"))
            if x.lower()=='y':
                pass
            elif x.lower()=='n':
                print("Thanks for playing!")
                print("Final score:",score)
                break
            elif x.lower()=='home':
                break
            else:
                print("Invalid Input!Taking back to Main Menu.")
                x='home'
                break
    else:
        print("Invalid Input! Try Again!")
