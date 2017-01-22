
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right
# Keep the game going until the user types 'exit'
# Keep track of how many guesses the user has taken, and when the game ends, print this out

import random
secret_number = random.randint(1,9)
print secret_number

attempt1_string = raw_input ('I have chosen a number between 1 and 9. Try to guess the number:')
count = 0

while attempt1_string != 'exit':
    attempt1_number = int(attempt1_string)
    count = count + 1
    if attempt1_number < secret_number:
        attempt1_string = raw_input('Try a bigger number:')
    elif attempt1_number > secret_number:
        attempt1_string = raw_input('Try a smaller number:')
    else:
        print 'Congratulations! You guessed right!'
        break

print 'You have guessed %d times.' % count
