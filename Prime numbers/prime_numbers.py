# Ask the user for a number and determine whether the number is prime or not.

number = input('Enter a number to check if it is prime or not:')

possible_divisors = range(2, number/2 + 1)
is_prime = True

for i in possible_divisors:
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print '%d is a prime number!' % number
else:
    print '%d is not a prime number!' % number
