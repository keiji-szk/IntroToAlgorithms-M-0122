# Set
# - a set of unique keys
# - not ordered
# - no duplicates (only unique elements)

s = {"apple", "banana", "cherry"}
# 1. create an empty set
# s = set()
# (because {} is considered empty dictionary in python)
print(type(s))
print(s)

l = [1, 1, 1, 1, 2, 3, 4, 5, 2, 3, 5, 5, 6, 8, 7, 7, 8, 7]
unique_set = set(l)
print(len(unique_set))

# set methods
# 1. add(elem)
unique_set.add(10)

# 2. `in` keyword to check if a set contains some value.
vowels = {"a", "e", "i", "o", "u"}
# vowels = ["a", "e", "i", "o", "u"]
print("a" in vowels)
# set if a lot faster than a list


# Collections in Python
# - str
# - list
# - tuple
# - dictionary
# - set

city = "vancouver"
print(list(city))
print(set(city))
