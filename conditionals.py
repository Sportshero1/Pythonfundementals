# conditional
# Method evaluate data
# if then else

import random

# ask the user to select the upper bound
upper_bound = input("What is the upper bound? ")
upper_bound = int(upper_bound)

# generate a random integer starting at 1 and going to upper_bound
random_number = random.randint(1,upper_bound)
print(random_number)

user_guess = None
# start and loop here
while user_guess != random_number:
    # ask the user to guess
    user_guess = input("Type a number between 1 and " + str(upper_bound) + ": ")

    # Check if user_guess == random_number

    if int(user_guess) == random_number:
        print("You win!")
    # user guess is not equal to random_number
    else:
         print("You lose!")
print("Game over")

# high_range = 100
# middle_number = int(high_range / 2)
# my_guess = middle_number
# number_guesses = 0
# highOrLow = "lower"
# output = "{} is {} than {}"

# my_random_number = random.randint(1,high_range)

# print(my_random_number)
# print(my_guess)


# # evaluate the random number and compare it the middle number
# if my_guess < my_random_number:
#     highOrLow = "lower"

# if my_guess > my_random_number:
#     highOrLow = "higher"

# print(output.format(my_guess, highOrLow, my_random_number))


# if my_random_number > my_guess:
#     print(my_random_number, "is greater than", my_guess)
# else:
#     print(my_random_number, "is less than", my_guess)
