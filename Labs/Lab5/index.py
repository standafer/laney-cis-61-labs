from math import sqrt, floor

# Q1: If This Not That
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer `this`.
    For each element in `i_list`, print the element if it is larger than `this`;
    otherwise, print the word "that".
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in range(len(i_list)):
        el = i_list[i]
        print(el if el > this else "that")

# Q2: Couple
def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2)
    
    # This could be getting the length or either s1 or s2, it doesn't matter
    coupled = []
    
    for i in range(len(s1)):
        coupled += [[s1[i], s2[i]]]
    
    return coupled

# Q3: Enumerate
def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    
    enumerated = []
    
    for i in range(len(s)):
        enumerated += [[i + start, s[i]]]
    
    return enumerated

# Q4: Squares only
def squares(s):
    """Returns a new list containing square roots of the elements of the original list
    that are perfect squares.
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    
    filtered = []
    
    for i in range(len(s)):
        el = s[i]
        root = sqrt(el)
        if floor(root) == root:
            # Integer
            filtered += [int(root)]
    
    return filtered

# Q5: Key of Min Value
def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """

    min_key = ""
    min = None

    for key in d:
        el = d[key]
        if not min or el < min:
            min = el
            min_key = key
    
    return min_key

# Q6: Flatten
def flatten(master_list):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    
    # Recursively expand into an accumulator
    def flatten_helper(accumulator, lst):
        for i in range(len(lst)):
            el = lst[i]
            
            if type(el) == list:
                flatten_helper(accumulator, el)
            else:
                accumulator += [el]
    
    flattened = []
    flatten_helper(flattened, master_list)
    
    return flattened

##### BEGIN DATA ABSTRACTION BOILER PLATE ########
def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

##### END DATA ABSTRACTION BOILERPLATE ########
# Extracted this out for code reuse
def city_coords_to_tuple(city):
    return get_lat(city), get_lon(city)

# Extracted into it's own function because it's reused in two places
# to keep it DRY
def distance_points(x1, x2, y1, y2):
    return sqrt(
        ((x1 - x2)**2) +
        ((y1 - y2)**2)
    )

def distance(city_a, city_b):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    
    city_a_lat, city_a_lon = city_coords_to_tuple(city_a)
    city_b_lat, city_b_lon = city_coords_to_tuple(city_b)

    # Distance formula:
    return distance_points(city_a_lat, city_b_lat, city_a_lon, city_b_lon)

def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    
    city_a_lat, city_a_lon = city_coords_to_tuple(city_a)
    city_b_lat, city_b_lon = city_coords_to_tuple(city_b)

    distance_a = distance_points(lat, city_a_lat, lon, city_a_lon)
    distance_b = distance_points(lat, city_b_lat, lon, city_b_lon)

    closest = city_a
    if distance_b < distance_a:
        closest = city_b
    
    return get_name(closest)