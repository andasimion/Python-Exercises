# Ask the user for a number and determine whether the number is prime or not.

def prime_number(num):
    possible_divisors = range(2, number/2 + 1)
    for i in possible_divisors:
        if num % i == 0:
            return False
    return True


number = input('Enter a number to check if it is prime or not:')

if prime_number(number):
    print "%d is a prime number!" % number
else:
    print "%d is not a prime number!" % number
