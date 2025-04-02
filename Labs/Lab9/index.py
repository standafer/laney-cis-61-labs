# BEGIN BOILERPLATE
class Link:
    empty = "I am empty!"
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches
    
def naturals():
    n = 1
    while True:
        yield n
        n += 1
# END BOILERPLATE

# Q1: Link to List
def link_to_list(link): 
    """Takes a linked list and returns a Python list with the same elements. 
    >>> link = Link(1, Link(2, Link(3, Link(4)))) 
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    # Link(1, Link(2, Link(3)))
    # terminator: doesn't have a rest. i.e. rest = Link.empty, but it does have a head/first
    if link == Link.empty:
        # nothing to return here
        return []
    # otherwise continue the same logic with the next value / "rest"
    # we can do this recursively.
    return [link.first] + link_to_list(link.rest)

# Q1B: Link to List (but iteratively)
def link_to_list_iteratively(link):
    """Takes a linked list and returns a Python list with the same elements iteratively.
    >>> link = Link(1, Link(2, Link(3, Link(4)))) 
    >>> link_to_list_iteratively(link)
    [1, 2, 3, 4]
    >>> link_to_list_iteratively(Link.empty)
    []
    """
    # Link(1, Link(2, Link(3)))
    result = []
    current = link

    # We know the iteration is done when the next link is empty (i.e. it is set to .rest and .rest is Link.empty)
    while current != Link.empty:
        result.append(current.first)
        current = current.rest
    
    return result

# Q2: Cumulative Sum
def cumulative_sum(t): 
    # check if it's a leaf node
    if len(t.branches) == 0:
        return t.label

    total = t.label
    for branch in t.branches:
        total += cumulative_sum(branch.label)
    
    t.label = total

    return total

# Q3: Scale
def scale(s, k): 
    """Yield elements of the iterable s scaled by a number k. 
    >>> s = scale([1, 5, 2], 5) 
    >>> list(s)
    [5, 25, 10]
    >>> m = scale(naturals(), 2) 
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """ 
    for item in s:
        yield item * k

# Q3B: Scale but using yield from
def scale_yield_from(s, k):
    yield from (item * k for item in s)