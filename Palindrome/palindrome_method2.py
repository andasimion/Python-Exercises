#Checking if a word is a palindrome using while loops.

word = raw_input('Enter a word:')
i = 0
j = len(word) - 1

while i<j and word[i] == word[j]:
    i = i + 1
    j = j - 1

if i >= j:
    print '%s is a palindrome' % word
else:
    print '%s is not a palindrome' % word
