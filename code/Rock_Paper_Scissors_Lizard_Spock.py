import random

# selection available are rock, paper and scissors
selection = ["rock", "paper", "scissors", "lizard", "spock"]

# ask the user_choice1 which they would like and store their choice
user_choice1 = input("Would you like rock, paper, scissors, lizard or spock: ")
print()

# have the user_choice2 select one of the choices 
user_choice2 = input("Would you like rock, paper, scissors, lizard or spock: ")

# print out the user_choice1 and user_choice2 selections
print(f"\nYou selected {user_choice1}, the other user selected {user_choice2}.\n")

# now it is time for the logic
# first check for a tie
if user_choice1 == user_choice2:
    print(f"\nYou both selected the same thing - it is a tie! What are the odds?")
# next check for user selection "rock"
elif user_choice1 == "rock":
    #for user_choice1 selection rock, check for user_choice2 selection scissors, lizard, spock or paper and if found report a win
    if user_choice2 == "scissors":
        print("Rock smashes scissors! You win!")
    elif user_choice2 == "lizard":
        print("Rock crushes lizard! You win!")
    #for user_choice1 selection rock and user_choice2 selection spock or paper, user_choice2 wins
    elif user_choice2 == "spock":
        print("Spock vaporizes rock! You lose!")
    else:
        print("Paper covers rock! You lose!")
# next check for user_choice1 selection "paper"
elif user_choice1 == "paper":
    # for user_choice2 selection paper and user_choice2 selection rock or spock user_choice1 wins
    if user_choice2 == "rock":
        print("Paper covers rock! You win!")
    elif user_choice2 == "spock":
        print("Paper disproves Spock! You win!")
    # for user_choice1 selection paper and user_choice2 selected scissors or lizard, user_choice2 wins
    elif user_choice2 == "lizard":
        print("Lizard eats paper! You lose!")
    else:
        print("Scissors cuts paper! You lose!")
# next check for user_choice1 selection "scissors"
elif user_choice1 == "scissors":
    # for user_choice1 selection scissors and user_choice2 selection paper or lizard user_choice1 wins
    if user_choice2 == "paper":
        print("Scissors cuts paper! You win!")
    elif user_choice2 == "lizard":
        print("Scissors decapitates lizard! You win!")
    # for user_choice1 selection scissors and user_choice2 selection spock or rock, user_choice2 wins
    elif user_choice2 == "spock":
        print("Spock smashes scissors! You lose!")
    else:
        print("Rock smashes scissors! You lose!")
elif user_choice1 == "lizard":
    # for user_choice1 selection lizard and user_choice2 selection spock or paper, user_choice1 wins
    if user_choice2 == "spock":
        print("Lizard poisons Spock! You win!")
    elif user_choice2 == "paper":
        print("Lizard eats paper! You win!")
    # for user_choice1 selection lizard and user_choice2 selection rock or scissors, user_choice2 wins
    elif user_choice2 == "rock":
        print("Rock crushes lizard! You lose!")
    else:
        print("Scissors decapitates lizard! You lose!")
elif user_choice1 == "spock":
    #for user_choice1 selection spock and user_choice2 selection scissors or rock, user_choice1 wins
    if user_choice2 == "scissors":
        print("Spock smashes scissors! You win!")
    elif user_choice2 == "rock":
        print("Spock vaporizes rock! You win!")
    #for user_choice1 selection spock and user_choice2 selection paper or lizard, user_choice2 wins
    elif user_choice2 == "paper":
        print("Paper disproves Spock! You Lose!")
    else:
        print("Lizard poisons Spock! You Lose!")
else:
    print("Invalid selection. Try again.")
