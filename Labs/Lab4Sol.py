""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    count = 0  # count the number of guesses
    lower = 1
    upper = 1000

    while True:
        guess = input(f"Enter your guess from {lower} to {upper}: ")
        if not guess.isdigit():
            print("Please enter an integer!")
            continue

        guess = int(guess)
        count += 1
        if guess < lower or guess > upper:
            print("Invalid input.")
            continue

        if guess == answer:
            print(f"You got it! The hidden number is {answer}")
            print(f"It took you {count} guess(es).")
            break
        elif guess > answer:
            upper = guess - 1
        else:
            lower = guess + 1
        print(f"Wrong! Guess count: {count}")


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()