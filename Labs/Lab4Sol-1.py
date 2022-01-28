""" Guessing Game """
import random


class RangeError(Exception):
    pass


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    lower_bound = 1
    upper_bound = 1000
    count = 0
    found = False
    while not found and lower_bound <= upper_bound:
        try:
            guess = int(input(f"Enter your guess from {lower_bound} to {upper_bound}: "))
            count += 1
            if guess < lower_bound or guess > upper_bound:
                raise RangeError
            if guess == answer:
                print(f"You got it! The hidden number is {guess}")
                print(f"It too you {count} guess(es).")
                break
            elif guess > answer:
                upper_bound = guess - 1
            else:
                lower_bound = guess + 1
            print(f"Wrong! Guess count: {count}")

        except RangeError:
            print(f"Please enter a number from {lower_bound} to {upper_bound}.")
        except ValueError:
            print("Invalid Input.")


if __name__ == '__main__':
    guessing_game()
