# string methods: functions that belong to string type
city = "vancouver"

# call, execute
print(city.capitalize())

upper = city.upper()
lower = city.lower()
print(lower)
print(upper)

# 1. .index(sub): returns the index of the first occurrence of substring, but if it doesn't exist, error!
print(city.index("v"))

# 2. .find(sub): returns the index of the first occurrence of substring, but if it doesn't exist, -1.
print(city.find("abc"))
print(city.find("van"))
print(city.find("v"))

# 3. .count(sub[, start, end])
# cast-sensitive
greetings = "Hello Hello Hello Hello Hello"
print(greetings.count("Hello", 10, 17))

# more string methods...
# (python official) https://docs.python.org/3/library/stdtypes.html
# https://www.w3schools.com/python/python_ref_string.asp
