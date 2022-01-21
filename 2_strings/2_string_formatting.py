food = "Sushi" "BBQ"
print(food)

# 'in' operator
# To check whether a string contains a specific substring
print("shi" in food)

# Escape Sequences ('\')
# \n: newline character
# \t: tab character
# \": double quote
# \\: backslash character
message = "\tHe says, \"how are you?\"\nI'm good!"
print(message)

phrase = """This is a really long string.
    Triple-quoted strings are used to define
multi-line strings."""
print(phrase)

# String formatting
# Format Specifiers
# %d: digit
# %s: string
# %f: float
# ...
name = "Derrick"
city = "Vancouver"
year = 2022
message1 = "Hello, Pycharm! My name is %s. I live in %s. It's %d!" % (name, city, year)
message2 = f"Hello, Pycharm! My name is {name}. I live in {city}. It's {year}!"
print(message1)
print(message2)

salary = 60000.12345
print("The average salary as a software developer is %.2f" % salary)
print("%-20.2f" % salary)
print("%20.2f" % salary)


# String interpolation (from 3.6 ~)
a = 3
b = 4
msg = f"{a} + {b} = {a + b}"
print(msg)


