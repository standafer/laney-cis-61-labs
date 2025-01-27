from math import pi

# Question 1
def twenty_twenty_five():
	"""Come up with the most creative expression that evaluates to 2025, 
	using only numbers and the +, *, and - operators.
	>>> twenty_twenty_five() 
	2025
	"""

	return ((10 * 10) + (10 * 5)) * (10 + 5) - (15 * 15)

# Question 2-1
def sphere_area(r):
    """Area of a sphere with radius r."""
    return 4 * pi * (r ** 2)

# Question 2-1
def sphere_volume(r):
    """ Volume of a sphere with radius r."""
    return (4/3) * pi * (r ** 3)

# Question 3
def alfonso_should_wear_jacket(current_temp, is_raining):
	return is_raining or current_temp < 60
