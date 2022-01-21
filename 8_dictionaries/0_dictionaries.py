# What is a a dictionary?
# - a 'set' of key:value pairs
# - not ordered (no index)
# - key must be unique

contacts = {
    "Derrick": "123-678-7890",
    "Keiji": "234-567-8901",
    "Pedro": ["123-098-1234", "754-213-5831"],
    7: "Hello"
}

# 1. access dictionary by key to get the value
print(contacts["Keiji"])
print(contacts["Derrick"])
print(contacts["Pedro"][1])
print(contacts[7])

# get the number of key:value pairs
print(len(contacts))

# 2. add a new entry (key-value pair)
contacts["Kaiya"] = "123-098-7652"
print(contacts)

# 3. update a value for existing key
contacts["Derrick"] = "778-123-1234"
print(contacts)
# Updating the dictionary with the entries from another dictionary
contacts.update({"K1": "V1", "K2": "V2"})

# 4. delete an entry from a dictionary
del contacts[7]
print(contacts)

# 5. Get all keys
print(list(contacts.keys()))
for k in contacts.keys():
    print(k)

# 6. Get all values
print(list(contacts.values()))
for v in contacts.values():
    print(v)

# 7. iterate through a dictionary with a (k, v)
print(list(contacts.items()))
for (k, v) in contacts.items():
    print(f"key: {k}, value: {v}")

# 8. Check if a dictionary contains a specific key
# `in` keyword
if "Derrick" in contacts:
    print("I have Derrick's contact info.")
else:
    print("I don't have Derrick's contact info.")

