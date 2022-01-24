# search_lab.py
# In this lab, you will be using two searching algorithms we covered in class to
# search for a word in dictionary. Compare the performance for each algorithm.
# You will have to output the number of steps for both algorithms when used for
# searching for the same word. (case-insensitive)
# Your output should look like this.

# Demo output
# Search word: {"orange"}
# Linear Search: found at {0}, took {0} steps
# Binary Search: found at {0}, took {0} steps
from searching.linear_search import linear_search
from searching.binary_search import binary_search

with open("words") as f:
    lines = f.readlines()
    # strip off the new line characters for each word in the list
    stripped = []
    for line in lines:
        w = line.strip().lower()
        stripped.append(w)

    target = input("Search word: ").lower()
    i, steps1 = linear_search(stripped, target)
    j, steps2 = binary_search(stripped, target)

    print(f"Linear Search: found at {i}, took {steps1} steps")
    print(f"Binary Search: found at {j}, took {steps2} steps")
