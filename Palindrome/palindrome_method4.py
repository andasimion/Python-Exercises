#Checking if a word is a palindrome using for loops.

word = raw_input('Enter a word: ')

for i in range(0,len(word)/2):
    if word[i] == word[len(word)-i-1]:
        is_palindrome = True
    else:
        is_palindrome = False
        break

if is_palindrome:
    print '%s is a palindrome' % word
else:
    print '%s is not a palindrome' % word
