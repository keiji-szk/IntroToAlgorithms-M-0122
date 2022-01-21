# range(start, end, steps): 'iterable', a sequence of integers


def mrange(start: int, end: int, steps: int = 1) -> list:
    """
    Returns a list of integers from start to end by steps
    ex) start <= i < end, skipped by steps
    mrange(1, 6) -> [1, 2, 3, 4, 5]
    mrange(1, 7, 2) -> [1, 3, 5]
    mrange(5, 10) -> [5, 6, 7, 8, 9]
    :param start: lower bound
    :param end: upper bound
    :param steps: steps to skip
    :return: a list of numbers within the range
    """
    res = []
    while start < end:
        res.append(start)
        start += steps

    return res


print(mrange(1, 6))
print(mrange(1, 7, 2))
print(mrange(5, 10))
for i in mrange(1, 10):
    print(i)


# *args
# take arbitrary number of arguments as Tuple
def xrange(*args) -> list:
    if len(args) == 1:
        return mrange(0, args[0])
    elif len(args) == 2:
        return mrange(args[0], args[1])
    elif len(args) == 3:
        return mrange(args[0], args[1], args[2])
    else:
        raise TypeError(f"range expected at most 3 arguments, got {len(args)}")


