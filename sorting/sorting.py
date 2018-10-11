'''
    This file contains the source code for heapsort, quicksort,
    merge sort, radix sort, and insertion sort. 
'''

import math


def main():
    array = [1005, 100, 5, 87, 905, 1983, 1, 42, 314]

    print("Radix sort")
    print(radix_sort(array))

    print("Insertion sort")
    print(insertion_sort(array))


def heap_sort(A):
    pass


def quick_sort(A):
    pass


def merge_sort(A):
    pass


def radix_sort(A):
    '''
        Radix sort can only be used if the data in the array are integers
        and non-negative numbers (unless modifications are made). It sorts 
        numbers by least-significant digit to most.

        Time complexity: O(n*d), where n is length of the array, d is number of digits
        Space complexity: O(n+k) where k is range of digits (0-9 => k = 10)
        Stable: yes
    '''

    # find the number of digits in the largest number in the array
    num_digits = math.floor(math.log10(max(A))) + 1

    # iterate through the digits from least significant to most
    for current_digit in range(num_digits):

        # create buckets to put the numbers in as we sort them
        buckets = [[] for _ in range(10)]

        # loop through the items to assign them to buckets
        for item in A:

            # add the item to the bucket that corresponds to the current digit we are sorting
            buckets[int((item/10**current_digit) % 10)].append(item)

        # iterate through the buckets and add the items back to the array in order
        index = 0
        for bucket in buckets:

            # iterate through each bucket's contents
            for item in bucket:
                A[index] = item
                index += 1

    return A


def insertion_sort(A):
    '''
        Insertion sort works by traversing through the array,
        left to right, while keeping a "sorted" section of the array
        to the left of a certain index. As a new value is reached, 
        you "insert" the value into the sorted section in a sorted order.

        The optimal time to use insertion sort is when N is small, or when
        the input array is nearly sorted, i.e. very few swaps are needed.
        When the input array is already sorted, insertion sort experiences its
        best case.

        Time complexity (average/worst case): O(n^2)
        Time complexity (best case): O(n)
        Stable: yes
    '''

    # loop from the 2nd element to the last element
    # no need to sort the first and last
    for i in range(1, len(A)):

        # retrieve the element we are going to "insert"
        key = A[i]
        # the index we are currently checking the key against
        j = i - 1

        # while we are not at the end of the array, and the value
        # at the index that we are checking against is bigger than
        # the key
        while j >= 0 and A[j] > key:

            # shift the current element one spot to the right
            A[j+1] = A[j]
            # look at the element to the left of the current
            j -= 1

        # insert the key into the current position of the j pointer
        A[j+1] = key

    return A


if __name__ == "__main__":
    main()
