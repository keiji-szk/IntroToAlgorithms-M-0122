# Bubble Sort - "Bubbling" up the largest element to the right!
# (pseudo-code)
#
# list = [...]
# for each scan from 0 to len(list) - 1
#     compare two adjacent elements
#     if the first element is greater than the second element
#         swap two elements

# Time Complexity: O(n^2)
# 1 + 2 + ... + n = n(n+1) / 2
# 1 + 2 + ... + n-1 = n(n-1) / 2

def bubble_sort(alist):
    steps = 0
    for scan in range(len(alist) - 1):
        swapped = False
        for j in range(len(alist) - 1- scan):
            steps += 1
            if alist[j] > alist[j + 1]:
                swapped = True
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp

        if not swapped:
            break

    print(f"total steps: {steps}")


if __name__ == '__main__':
    l = [5, 1, 3, 2, 4, 0]
    bubble_sort(l)
    print(l)
