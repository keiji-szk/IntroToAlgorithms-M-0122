# loop? to repeat code
# A while-loop is similar to an if-statement
# It executes some code if some condition is true.
# It will continue to execute the code as long as (while) the condition is true.

# Syntax
# while __condition__:
#     do something

# print number from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1
print("Hello")


# Exercise
# print all squares from 1 <=  <= 99. (1, 4, 9, 16, 25, ..., 81)
n = 1
while n * n < 100:
    print(n * n)
    n += 1

# print all even numbers from 1 <=  <= 100. (2, 4, ..., 100)
n = 2
while n <= 100:
    print(n)
    n += 2
