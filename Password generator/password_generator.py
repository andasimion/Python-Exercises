# Write a password generator. Ask the user how strong they want their password to be.
# For weak passwords, pick a word or two from a list.
# Strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user
# asks for a new password. Include your run-time code in a main method.

import random
import string

def pass_generator(word):
    if word == 'weak password':
        weak_password = ''.join(random.choice(['black', 'cat', 'white', 'bacon',
        'slayer', 'racoon', 'spring', 'python']) for i in range(2))
        return weak_password
    elif word == 'strong password':
        strong_password = ''.join(random.choice(string.ascii_uppercase +
        string.ascii_lowercase + string.digits + string.punctuation) for x in range(10))
        return strong_password

def main():
    password = raw_input('Do you prefer a weak password or a strong password?: ')
    if password == 'weak password' or password == 'strong password':
        print pass_generator(password)
    else:
        print 'Choose again what type of password do you want!'

if __name__ == '__main__':
    main()
