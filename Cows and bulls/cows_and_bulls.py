# Create a program that will play the 'cows and bulls' game with the user.
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a 'cow'.
# For every digit the user guessed correctly in the wrong place is a 'bull'.
# Every time the user makes a guess, tell them how many 'cows' and 'bulls' they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

secret_number = str(random.randint(1000,9999))
print secret_number

def cows_count(num):
    count_cows = 0
    for i in range(len(secret_number)):
        if secret_number[i] == num[i]:
            count_cows = count_cows + 1
    return count_cows

def bulls_count(num):
    count_bulls = 0
    for i in range(len(secret_number)):
        if num[i] in secret_number and num[i] != secret_number[i]:
            count_bulls = count_bulls + 1
    return count_bulls

def main():
    number_attempt1 = raw_input('Choose a 4-digit number: ')
    count = 1
    while True:
        if len(number_attempt1) != len(secret_number):
            print 'Enter a 4-digit number!'
            number_attempt1 = raw_input('>  ')
            count = count + 1
        elif secret_number != number_attempt1:
            print cows_count(number_attempt1), 'cows'
            print bulls_count(number_attempt1), 'bulls'
            number_attempt1 = raw_input('Try again: ')
            count = count + 1
        else:
            print 'Congratulation! You guessed the number!'
            print 'You guessed the number in %s tries.' % count
            break


if __name__ == '__main__':
    main()
