# function?
# - a reusable piece of code you can run over and over again
# - take some input (arguments), return ouput

# f(x) = x + 2
# 1. define a function
def f(x: int) -> int:  # function header (prototype)
    # function body
    return x + 2


# 2. call(invoke) a function
res = f(10)
print(res)


def print_one():
    print(1)


a = print_one()
print(a)


def print_menu():
    print("===== Menu =====")
    print("| 1. Burger    |")
    print("| 2. Pizza     |")
    print("| 3. Feijoada  |")
    print("| 4. Ramen     |")
    print("| 5. Knedlik   |")
    print("================")


for i in range(5):
    print_menu()


def get_fullname(fn: str, ln: str) -> str:
    return fn + " " + ln


full = get_fullname("Derrick", "Park")
print(full)
print(get_fullname("Justin", "Bieber"))


# Exercise
# define a function that takes one integer and returns whether
# the integer is even or not.

def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


# def is_even(n: int) -> bool:
#     return n % 2 == 0

print(is_even(10))
print(is_even(7))
