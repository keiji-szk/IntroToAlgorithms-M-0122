import math
import time


def is_prime_naive(n: int) -> bool:
    """ Time Complexity: O(n) """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime(n: int) -> bool:
    """ Time Complexity: O(sqrt(n)) """
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


if __name__ == "__main__":
    start_time = time.time()
    l = generate_primes(500000)
    end_time = time.time()
    print(f"{end_time - start_time} seconds.")

