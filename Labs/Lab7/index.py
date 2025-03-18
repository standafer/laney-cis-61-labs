# Q1 - Add This Many
def add_this_many(x, el, lst): 
    """ Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(2, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    # append el to the end of lst based on the number of times x occurs in lst
    # we use a range instead of generic iteration because if we kept iterating while
    # we kept adding it would continue this forever
    for i in range(len(lst)):
        element = lst[i]

        if element == x:
            lst.append(el)

# Q2 - Group By
def group_by(seq, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    groups = {}

    for element in seq:
        group = fn(element)

        if not group in groups:
            groups[group] = []

        groups[group].append(element)

    return groups

# Q3: Make Adder Increasing
def make_adder_inc(n):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2) 
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """

    incrementor = 0
    def adder(x):
        nonlocal incrementor

        sum = n + x + incrementor
        incrementor += 1

        return sum

    return adder

# Q5 - Memory
def memory(n): 
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    
    value = n
    def mutate(func):
        nonlocal value
        value = func(value)
        return value
    return mutate

# Q6: Next Fibonacci
def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.
    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    num_a = 0
    num_b = 1
    
    def next_fib():
        nonlocal num_a, num_b

        result = num_a
        num_a, num_b = num_b, num_a + num_b

        return result
    
    return next_fib

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """

    invalid_attempts = []

    def withdraw(amount, provided_password):
        nonlocal balance, invalid_attempts, password
        
        if len(invalid_attempts) >= 3:
            return f"Your account is locked. Attempts: {invalid_attempts}"
        elif provided_password != password:
            invalid_attempts.append(provided_password)
            return "Incorrect password"
        else:
            if amount > balance:
                return 'Insufficient funds'
            
            balance = balance - amount
            
            return balance
    
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    verification = withdraw(0, old_password)
    
    if type(verification) == str:
        return verification
    
    def joint_withdraw(amount, password):
        if password == new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, password)
    
    return joint_withdraw