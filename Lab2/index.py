from operator import add, sub
from math import floor

# Q1: Fix the Bug
def both_positive(x, y):
	"""Returns True if both x and y are positive.
	>>> both_positive(-1, 1)
	False
	>>> both_positive(1, 1)
	True
	"""
	return x > 0 and y > 0

# Q2: A Plus Abs B
def a_plus_abs_b(a, b):
	"""Return a+abs(b), but without calling abs.
	>>> a_plus_abs_b(2, 3)
	5
	>>> a_plus_abs_b(2, -3)
	5
	"""

	if b < 0:
		f = lambda a, b: a - b
	else:
		f = lambda a, b: a + b

	return f(a, b)

# Q3: Two of Three
def two_of_three(a, b, c):
	"""Return x*x + y*y, where x and y are the two largest members of the
	positive numbers a, b, and c.
	>>> two_of_three(1, 2, 3)
	13
	>>> two_of_three(5, 3, 1)
	34
	>>> two_of_three(10, 2, 8)
	164
	>>> two_of_three(5, 5, 5)
	50
	"""
	return (max(a, b) == a) and (a**2) + (max(b, c)**2) or (b**2) + (max(a, c)**2)

# Q4: Largest Factor
def largest_factor(n):
	"""Return the largest factor of n that is smaller than n.
	>>> largest_factor(15) # factors are 1, 3, 5
	5
	>>> largest_factor(80) # factors are 1,2,4,5,8,10,16,20,40
	40
	>>> largest_factor(13) # factor is 1 since 13 is prime
	1
	"""
	checking = 1
	largest = checking
	while (checking < n):
		if (n % checking == 0):
			# No remainder, goes in evenly, meaning this is the new largest
			largest = checking
		checking += 1

	return largest

# Q5: Sum Digits
def sum_digits(n):
	"""Sum all the digits of n.
	>>> sum_digits(10) # 1 + 0 = 1
	1
	>>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
	12
	>>> sum_digits(1234567890)
	45
	>>> x = sum_digits(123) # make sure that you are using return rather than print
	>>> x
	6
	"""
	sum = 0
	while n > 0:
		sum += n % 10
		n = floor(n / 10)
	return sum

# Q6: Hailstone
def hailstone(n):
	while (True):
		print(n)
		if (n == 1): break
		if (n % 2 == 0):
			# Even number
			n = int(n / 2)
		else:
			# Odd number
			n = int((n * 3) + 1)

# Q7: Fibonacci Number
def fibonacciN(n):
	"""Return the nth Fibonacci number.
	Fibonacci Numbers is a series of numbers in which each number is 
	the sum of the two preceding numbers
	>>> fibonacciN(5) # 1, 1, 2, 3, 5
	5
	>>> fibonacciN(7) 
	13
	"""
	num_a, num_b = 0, 1
	count = 0

	while count < n:
		num_a, num_b = num_b, num_a + num_b
		count += 1
	return num_a

# Q8: Is Prime?
def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	
	divisor = n - 1
	
	while (divisor > 1):
		if (n % divisor == 0):
			return False
		divisor -= 1
	return True
