while True:  # This makes your code repeat forever,
    # to make it easier for you to keep testing it out with different values

    # You may assume the input will be valid
    # e.g. Your program does not have to work if someone gives an n that is
    #      bigger than the total number of digits in number. Your code must
    #      only work correctly for valid input.
    number = int(input("Please give an integer number: "))  # this asks the user for input and then stores the user
    # input as an int into our variable.
    n = int(input("Which position's digit do you want? "))

    # 1. simple arithmetic
    print((number // (10 ** (n - 1))) % 10)

    # 2. string index
    # s = str(number)
    # print(s[len(s) - n])

    # 3. loop
    # while n > 1:
    #     number = number // 10
    #     n -= 1
    # print(number % 10)



