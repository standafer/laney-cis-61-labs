import math

# def sum_up_to(n, current_n=0, summation=0):
#     assert n, "expected n"

#     if current_n <= n:
#         return sum_up_to(n, current_n + 1, summation + current_n)
#     else:
#         return summation
        
# print(sum_up_to(10))

def count_up(n):
    if n != 1:
        count_up(n-1)
    print(n)

count_up(10)

def sum_digits(n):
    digits = len(str(n))