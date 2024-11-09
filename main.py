import math
from ast import Param
from itertools import combinations

"""
Create a Python(or Pseudo Python) function that solves how many non-negative integer solutions there
are in a linear equation in the form:
x1 + x2 + x3 + x4 +... + xℓ = S
Where each xi variable may have some restriction on its value. The less than or equal to constraints
are stored in a list lower constraints (0 is stored if there is no constraint). The upper bound
constraints are stored in the list upper constraints as PAIRS: (i, k) indicating that xi ≤ k, and
len(upper constraints)≤3. [Hint: Be careful of double constraints (eg. 3 ≤x2 ≤8)]
"""

def choose(n, k):
    return math.comb(n, k)

def negate(b):
    """x_n ≤ b ==> x_n ≥ b"""
    return b - 1


def number_of_solutions(l, s):
    # l: represents the number of terms in the equations
    # s: represents the number of cookies to distribute x1 + x2 ... = s
    global lower_constraints, upper_constraints
    cookies = s
    bars = l - 1
    possible_equations_count = 0

    ranges = [ [lower_constraints[i], s] for i in lower_constraints]

    for i in range(len(upper_constraints)):
        index = upper_constraints[i][0]
        max_val = upper_constraints[i][1]

        ranges[index][1] = max_val

    print(ranges)

    unrestricted_total = choose(cookies + bars, bars)

    # now each term is in the form a ≤ x_n ≤ b

    for _range in ranges:
        combinations = unrestricted_total - choose( cookies - negate(_range[1]) + bars, bars)
        possible_equations_count += combinations

    return possible_equations_count


def test():
    global lower_constraints, upper_constraints

    count = 0

    for a in range(7, 17):
        for b in range(0, 17):
            for c in range(0, 17):
                for d in range(0, 17):
                    if a + b + c +d == 17:
                        count += 1
    return count







if __name__ == "__main__":
    LENGTH = 4
    VALUE = 17

    lower_constraints = [0, 0, 0, 0]
    upper_constraints = [[1, 7]]


    print(
        number_of_solutions(LENGTH, VALUE),
        test()
    )
