# Conditional Statement (if-else)
# if __condition__:
#     do something
# elif __condition__:
#     do something
# else:
#     do something

# input(prompt) - takes a prompt message and returns user input as a string
age = int(input("Enter your age: "))

# indentation (spaces)
if age >= 18:
    print("You can start drinking...")
elif 15 <= age < 18:
    print("High school student")
elif 13 <= age < 15:
    print("Junior-high school student")
elif 7 <= age < 13:
    print("Elementary school student")
elif 5 <= age < 7:
    print("Kindergarten")
else:
    print("Baby")