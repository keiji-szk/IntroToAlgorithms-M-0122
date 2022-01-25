"""
 String, List - Level 2.0
"""


def count_hi(string: str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    count = 0
    for i in range(len(string) - 1):
        if string[i:i+2] == "hi":
            count += 1
    return count


def cat_dog(string: str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return string.count("cat") == string.count("dog")


def count_code(string: str):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    count = 0
    for i in range(len(string) - 3):
        if string[i:i+2] == "co" and string[i+3] == "e":
            count += 1
    return count


def end_other(a: str, b: str):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    lower_a = a.lower()
    lower_b = b.lower()
    len_a = len(lower_a)
    len_b = len(lower_b)
    if len_a < len_b:
        return lower_b[len_b - len_a:] == lower_a
    else:
        return lower_a[len_a - len_b:] == lower_b


def count_evens(nums: [int]):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    # return len([num for num in nums if num % 2 == 0])
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


def big_diff(nums: [int]):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    return max(nums) - min(nums)


def sum13(nums: [int]):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    i = 0
    total = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums: [int]):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    total = 0
    add_switch = True
    for num in nums:
        if num == 6 and add_switch:
            add_switch = False
            continue
        if num == 7 and not add_switch:
            add_switch = True
            continue
        if add_switch:
            total += num

    return total


def has22(nums: [int]):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
