# Binary Search
# - "sorted" list of items
# - Keep comparing the middle item in the list to the target
#   while removing the half of the list from the search range.
# - Time Complexity: O(lg N)
import random


def binary_search(items: [str], target: str) -> (int, int):
    """
    Returns the index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    Using binary search algorithm
    Time Complexity: O(lg N)
    :param items: a list of sorted items
    :param target: the item we're searching for
    :return: the index of the target in the items if the target exists, otherwise - 1.
    """
    lower = 0
    upper = len(items) - 1
    steps = 0
    while lower <= upper:
        mid = (lower + upper) // 2
        steps += 1
        if items[mid] == target:
            return mid, steps
        elif items[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1, steps


if __name__ == '__main__':
    countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
                 "France", "Germany", "Honduras", "Italy", "Japan",
                 "Korea", "Latvia", "Malaysia", "Norway", "Oman", "Poland",
                 "Qatar", "Russia", "Spain", "Thailand", "USA", "Vietnam",
                 "Wales", "Yemen", "Zambia"]

    # lg 26 = 4.xxx
    target = "Apple"
    pos, steps = binary_search(countries, target)
    print(f"Found {target} at {pos} index in {steps} steps.")

    # Generate a list of 100 random numbers
    # search_items = random.sample(range(1, 1000), 100)
    # search_items.sort()
    #
    # print(f"search_items: {search_items}")
    # target_index = random.randint(0, 99)
    # print(f"target_index: {target_index}")
    # target = search_items[target_index]
    # print(f"target: {target}")
    #
    # print(binary_search(search_items, 150))

