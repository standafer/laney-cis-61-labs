# Lab 1: Skip Add
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.
    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30"""
    if n < 1:
        return 0
    else:
        return n + skip_add(n - 2)

# Lab 2: Hailstone
def hailstone(n):
    """ Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))
    if n == 1:
        return int(n)
    elif n % 2 == 0:
        return int(1 + hailstone(n / 2))
    else:
        return int(1 + hailstone((n * 3) + 1))

# Lab 3: Summation
def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    """
    if n == 0:
        return n
    else:
        return term(n) + summation(n - 1, term)

# Q4: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def is_prime_helper(n, divisor=2):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True

        return is_prime_helper(n, divisor + 1)
    
    return is_prime_helper(n)

# Q5: GCD
def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Count Stairs
def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(5)
    8
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

# Count Stairs - recursive
def count_k(n, k):
    """ 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total