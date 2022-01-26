# Selection Sort
# (pseudo-code)
# For each scan from 0 to len(A)
#     Find the min element (linear search)
#     Swap the min element with A[scan]

# Time Complexity: O(n^2)

def selection_sort(alist):
    for scan in range(len(alist) - 1):
        min_index = scan
        for i in range(scan + 1, len(alist)):
            if alist[i] < alist[min_index]:
                min_index = i

        if min_index != scan:
            temp = alist[min_index]
            alist[min_index] = alist[scan]
            alist[scan] = temp


if __name__ == '__main__':
    A = [5, 1, 4, 2, 3]
    selection_sort(A)
    print(A)


