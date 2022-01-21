# List - A sequence of any data type items (elements)

# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]
print(squares)

# 2. list operations
squares += [64, 81]  # add two elements at the end of the list
print(squares)

l = [1, "Hello", True, 3.14, [1, 2]]
print(l * 2)
print(l[4][0])  # the first element of the list [1, 2]

# 3. Indexing a list
print(squares[2])
print(squares[-1])
print(squares[len(squares) - 1])
print(len(squares))

# Slicing a list (sublist)
print(squares[:3])
print(squares[3:])
squares[5:8] = []
print(squares)

# 4. list methods
countries = ["Canada", "Canada", "Brazil", "Japan", "Canada", "Taiwan", "Czech Republic", "Mexico", "Chile", "USA", "Germany", "Turkey"]

# .append(item): adds item at the end of the list
countries.append("France")
print(countries)

# .insert(index, item): inserts item at the given index
countries.insert(0, "Korea")
print(countries)

# .remove(item): removes item from the list
countries.remove("Turkey")
print(countries)

# .pop(index): removes(pops) the item at the given index
countries.pop(0)
print(countries)

# .index(item): returns the index of the item
print(countries.index("Brazil"))

# .count(item): returns the number of the given item in the list
print(countries.count("Canada"))


# String vs List
# Strings are IMMUTABLE (cannot change)
# Lists are MUTABLE
city = "Vancouver"
# city[0] = "B"
l = ["Vancouver", "Burnaby", "Surrey", "Richmond", "Coquitlam"]
l[2] = "Maple Ridge"
print(l)