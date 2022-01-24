# * Searching
# - a list of items (collection), a target

# Linear Search?
# - "unsorted" list of data
# - search for the target in a linear manner (one by one)
# - In the worst case, it will take n steps for n elements
# - Time Complexity: O(n)
import random


def linear_search(items: [str], target: str) -> (int, int):
    """
    Returns the index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    :param items: a list items
    :param target:  the item we're looking for
    :return: the index of the target in the items if the target exists, otherwise -1.
    """
    steps = 0
    for i in range(len(items)):
        steps += 1
        if items[i] == target:
            return i, steps

    return -1, steps


if __name__ == '__main__':
    # Generate a list of 100 random numbers
    search_items = random.sample(range(1, 1000), 100)
    print(f"search_items: {search_items}")
    target_index = random.randint(0, 99)
    print(f"target_index: {target_index}")
    target = search_items[target_index]
    print(f"target: {target}")

    print(linear_search(search_items, target) == target_index)
    print(linear_search(search_items, 150))


