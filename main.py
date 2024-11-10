import math

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

def number_of_solutions(lower_constraints, upper_constraints, value, length):
    cookies = value - sum(lower_constraints)
    bars = length - 1

    if bars < 0:
        bars = 0

    sols_w_lower = choose(cookies + bars, bars)

    upper_constraints_count = len(upper_constraints)

    if upper_constraints_count == 0:
        return sols_w_lower
    elif upper_constraints_count == 1:
        pass
    elif upper_constraints_count == 2:
        pass
    elif upper_constraints_count == 3:
        pass

if __name__ == "__main__":
    lower_constraints = [2, 3, 4, 2, 0]
    upper_constraints = []
    VALUE = 30
    LENGTH = 5


    print(
        number_of_solutions(lower_constraints, upper_constraints, VALUE, LENGTH)
    )
