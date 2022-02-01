# What does the code below do? Write a comment explaining each line for Drawing 1.

n = int(input("Choose a number: "))

# Drawing Example
# for row in range(n):  # for each row
#     for column in range(row+1):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()

# Drawing 1
# YOUR CODE BELOW (feel free to comment out previous drawings to make newer ones more clear)
for i in range(n):
    # print spaces stars
    print(f"{' ' * (n - (i + 1))}{'*' * (2 * i + 1)}")


# Drawing 2
for row in range(n, 0, -1):
    for col in range(row):
        print("*", end="")
    print()


# Drawing 3
for i in range(n // 2 + 1):
    print("*" * (i + 1))

for i in range(n // 2):
    print("*" * (n // 2 - i))

# Drawing 4



# Drawing 5





