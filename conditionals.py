# conditional
# Method evaluate data
# if then else

import random

high_range = 100
middle_number = int(high_range / 2)
my_guess = middle_number
number_guesses = 0
highOrLow = "lower"
output = "{} is {} than {}"

my_random_number = random.randint(1,high_range)

print(my_random_number)
print(my_guess)


# evaluate the random number and compare it the middle number
if my_guess < my_random_number:
    highOrLow = "lower"

if my_guess > my_random_number:
    highOrLow = "higher"

print(output.format(my_guess, highOrLow, my_random_number))


if my_random_number > my_guess:
    print(my_random_number, "is greater than", my_guess)
else:
    print(my_random_number, "is less than", my_guess)


