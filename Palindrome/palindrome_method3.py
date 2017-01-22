#Checking if a word is a palindrome using while loops.

word = raw_input('Enter a word: ')
i = 0
is_palindrome = True

while i<len(word)/2 and is_palindrome:
    if word[i] != word[len(word)-i-1]:
        is_palindrome = False
    i = i + 1

if is_palindrome:
    print '%s is a palindrome' % word
else:
    print '%s is not a palindrome' % word
