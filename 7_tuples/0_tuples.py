# Tuples are almost identical to lists.
# The only big difference between lists and tuples is that
# tuples cannot be modified (immutable).
# Tuples, you can NOT add(append), change(replace), or delete(remove)
# elements from the tuple.

vowels = ("a", "e", "i", "o", "u")
# vowels[0] = "v"
print(vowels[0])
print("k" in vowels)

# methods
print(vowels.index("i"))
print(vowels.count("a"))

# Use cases
# 1. return multiple values from a function


def split_name(name: str) -> (str, str):
    fullname = name.split(" ")
    first = fullname[0]
    last = fullname[1]
    return first, last


# 2. multiple assignments
fn, ln = split_name("Derrick Park")
print(ln)
print(fn)

# 3. constant list of data
livable_provinces = ("BC", "ON", "AB", "QC")


# swap!
a = 10
b = 20

temp = b
b = a
a = temp

print(a)
print(b)

# only python way
x = 50
y = 70

x, y = y, x
print(x)
print(y)