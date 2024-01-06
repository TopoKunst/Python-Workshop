
"""
Q3: Lambdas and Currying
"""
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    # return lambda op: lambda x: lambda y: op(x, y)
    return lambda x: lambda y: func(x, y)

# test
# from operator import add, mul, mod
# print(lambda_curry2(add)(3)(5))
# print(lambda_curry2(mul)(5)(42))
# print(lambda_curry2(mod)(123)(10))


"""
Q4: Count van Count
"""
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda n: sum([condition(n, i) for i in range(1, n+1)])

# test
# count_factors = count_cond(lambda n, i: n % i == 0)
# print(count_factors(2))
# print(count_factors(4))
# print(count_factors(12))
# is_prime = lambda n, i: count_factors(i) == 2
# count_primes = count_cond(is_prime)
# print(count_primes(2))
# print(count_primes(3))
# print(count_primes(4))
# print(count_primes(5))
# print(count_primes(20))


"""
Q7: Composite Identity Function
"""
def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    fg = compose1(f, g)
    gf = compose1(g, f)
    return lambda x: fg(x) == gf(x)

# test
# add_one = lambda x: x + 1
# square = lambda x: x**2
# b1 = composite_identity(square, add_one)
# print(b1(0))
# print(b1(4))



def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def cycle_with_n(n):
        resf = lambda x: x
        p = n // 3
        q = n % 3
        for i in range(p):
            f = compose1(f3, compose1(f2, f1))
            resf = compose1(f, resf)
        if q == 0:
            return resf
        elif q == 1:
            return compose1(f1, resf)
        else:
            return compose1(compose1(f2, f1), resf)

    return cycle_with_n

# test
# def add1(x):
#     return x + 1
# def times2(x):
#     return x * 2
# def add3(x):
#     return x + 3
# my_cycle = cycle(add1, times2, add3)
# identity = my_cycle(0)
# print(identity(5))
# add_one_then_double = my_cycle(2)
# print(add_one_then_double(1))
# do_all_functions = my_cycle(3)
# print(do_all_functions(2))
# do_more_than_a_cycle = my_cycle(4)
# print(do_more_than_a_cycle(2))
# do_two_cycles = my_cycle(6)
# print(do_two_cycles(1))