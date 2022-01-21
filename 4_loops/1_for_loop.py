# For loops are used to iterate over a given 'sequence'.
# On each iteration, the variable (loop variable) defined in
# the for loop will be assigned to the next value (sequence).

# 1. string - a sequence of characters
city = "Vancouver"

for i in city:
    print(i)

i = 0
while i < len(city):
    print(city[i])
    i += 1


# 2. range(): a sequence of numbers
# range(end) - 0 <=   < end
# range(10) - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i)


print("================================")
# range(start, end) - start <=   < end
# range(5, 10) - 5, 6, 7, 8, 9
for i in range(5, 10):
    print(i)

print("================================")
# range(start, end, steps=1)
# range(1, 101, 2) - 1, 3, 5, 7, ..., 99
for i in range(1, 101, 2):
    print(i)

print("================================")
# print 100, 99, 98, ..., 1
for i in range(100, 0, -1):
    print(i)


# Exercise (for-loop)
# 1. print all odd numbers from 0 to 100
for i in range(101):
    if i % 2 == 1:
        print(i)


# 2. print all even numbers from 0 to 100
for i in range(101):
    if i % 2 == 0:
        print(i)


# 3. Count the number of vowels (a, e, i, o, u, A, E, I, O, U)
word = "Vancouver"
count = 0
for i in word:
    if i in "aeiouAEIOU":
        count += 1

print(count)

# list - a sequence of items
countries = ["Canada", "Brazil", "Japan", "Taiwan", "Czech Republic", "Mexico", "Chile", "USA", "Germany", "Turkey"]
for i in countries:
    print(i)