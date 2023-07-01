#!/usr/bin/python3
""" finding the peak of an unsorted list of ints """
def find_peak(list_of_integers):
    n = len(list_of_integers)

    if n == 0:
        return None

    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
