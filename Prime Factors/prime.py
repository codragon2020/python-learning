#!/usr/bin/env python3

# Prime Factorization
# Have the user enter a number
# and return its prime factors

# Extra: show the exponent of
# the prime factors as well

from collections import Counter

def isPrime(x):
    """
    Checks whether the given
    number x is prime or not
    """
    # 2 is prime
    if x == 2:
        return True
    
    # All even numbers except for 2 are not prime
    # Anything less than 2 is not prime
    if (x % 2 == 0) or (x < 2):
        return False

    # start with 3, check for the sqr root of x 
    # stepping by 2 optimizes the results by testing only the odd numbers
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def getExponent(n):
    """
    Counts the same elements in n list
    returns a list with the exponent of
    the multiple elements
    """

    c = Counter(n)
    factors = []

    for i in range(min(n), max(n) + 1):
        if i in n:
            if c[i] != 1:
                factors.append(str(i) + '^' + str(c[i]))
            else:
                factors.append(str(i))

    return factors

def main():  # Wrapper function

    n = int(input('Enter a number to find its prime factors: '))

    factors = []
    counter = 2

    while True:

        if n == 0 or n == 1:
            break

        for i in range(counter, n + 1):
            if n % i == 0:
                if isPrime(i):
                    factors.append(i)
                    n //= i
                    break

    if len(factors) != 0:
        factors = getExponent(factors)
        print(', '.join(factors))
    else:
        print('The number', n, 'does not have any prime factors.')

if __name__ == '__main__':
    main()