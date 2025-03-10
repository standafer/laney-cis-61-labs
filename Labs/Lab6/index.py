### BEGIN BOILERPLATE ###
#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Test Trees
t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
t3 = tree(8,
          [tree(4,
                [tree(2), tree(3)]),
           tree(3,
                [tree(1), tree(1,
                               [tree(1), tree(1)])])])
### END BOILERPLATE ###
### BEGIN CUSTOM BOILERPLATE ###
def print_tree(t, indent=0):
    """
    Print a tree structure with indentation to visualize the hierarchy.
    
    Args:
        t: The tree to print
        indent: The current indentation level (default: 0)
    """
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 2)
### END CUSTOM BOILERPLATE ###

# Q1: Acorn Finder
def acorn_finder(t):
    """Returns True if t contains a node with the value 'acorn' and False otherwise.
    >>> scrat = tree('acorn')
    >>> acorn_finder(scrat)
    True
    >>> sproul=tree('roots',[tree('branch1',[tree('leaf'),tree('acorn')]), tree('branch2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """

    # Base case
    if label(t) == "acorn":
        return True

    # Check all branches
    for branch in branches(t):
        if acorn_finder(branch):
            return True
    
    # Otherwise, no acorn for the squirrels
    return False

# Q2: Pruning Leaves
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears 
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """

    # Illegal value, skip.  
    if is_leaf(t) and label(t) in vals:
        return None

    # Build the tree taking advantage of the fact that the
    # function performs the validity checks for leaves
    return tree(
        label(t),
        [
            sanitized_branch for sanitized_branch in [
                prune_leaves(branch, vals) for branch in branches(t)
            ] if sanitized_branch
        ]
    )

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    
    if is_leaf(t):
        # If it's a leaf, add the vals to the childrenx
        return tree(label(t), [tree(val) for val in vals])
    else:
        return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])

# Q4: Height of a Tree
def height(t): 
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2
    """
    
    if is_leaf(t):
        return 0
    
    # Get the maximum depth
    return 1 + max([ height(branch) for branch in branches(t) ])

# Q5: Double_Tree
def double_tree(t): 
    """Return a tree with the square of every element in t 
    >>> numbers = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7)]), tree(8)])])
    >>> print_tree(double_tree(numbers)) 
    2
      4
        6
        8
      10
        12
          14
        16
    """

    return tree(label(t)*2, [ double_tree(branch) for branch in branches(t) ])