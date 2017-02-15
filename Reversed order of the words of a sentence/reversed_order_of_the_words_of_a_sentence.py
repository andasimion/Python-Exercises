# Write a program that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order

string_words = raw_input('Enter a sentence:')

def reversed_sentence (sentence):
    for i in sentence:
        stripped_sentence = sentence.strip()
        word = stripped_sentence.split(' ')
    reversed_words = ' '.join(list(reversed(word)))
    return reversed_words

print reversed_sentence(string_words)
