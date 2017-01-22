#Ask the user for a string and print out whether
# this string is a palindrome or not.
#A palindrome is a string that reads the same forwards and backwards.

word = raw_input('Enter a word: ')
reverse_word = word[::-1]

if word == reverse_word:
    print '%s is a palindrome.' % word
else:
    print '%s is not a palindrome.' % word
