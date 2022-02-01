""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist: list):
    # 1. split the list
    first_half = alist[:len(alist)//2]
    second_half = alist[len(alist)//2:]
    # 2. selection sort the first half
    selection_sort(first_half)
    # 3. selection sort the second half
    selection_sort(second_half)
    # 4. combine both and return
    return first_half + second_half[::-1]


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

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


# Time complexity: O(n)
def merge_two(A, B):
    i = 0
    j = 0
    merged = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    if i == len(A):
        return merged + B[j:]
    else:
        return merged + A[i:]


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    for i in range(len(mylist)):
        if mylist[i] < 0:
            mylist[i] = 0
    return mylist

