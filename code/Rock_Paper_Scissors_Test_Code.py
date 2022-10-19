import random

# selection available are rock, paper and scissors
selection = ["rock", "paper", "scissors"]

# ask the user which they would like and store their choice
user_choice = input("Would you like rock, paper or scissors: ")

# have the computer select one of the choices randomly
computer_choice = random.choice(selection)

# print out the user and computer selections
print(f"\nYou selected {user_choice}, the computer selected {computer_choice}.\n")

# now it is time for the logic
# first check for a tie
if user_choice == computer_choice:
    print(f"\nYou both selected the same thing - it is a tie!")
# next check for user selection "rock"
elif user_choice == "rock":
    #for user selection rock, check for computer selection scissors and if found report a win
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
# next check for user selection "paper"
elif user_choice == "paper":
    # for user selection paper and computer selection rock, user wins
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    # for user selection paper and ocmputer selected scissors
    else:
        print("Scissors cuts paper! You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
else:
    print("Invalid selection. Try again.")
