'''
    This file contains the source code for heapsort, quicksort,
    merge sort, radix sort, and insertion sort. 
'''

import math


def main():
    array = [1005, 100, 5, 87, 905, 1983, 1, 42, 314]

    print("Radix sort")
    print(radix_sort(array))


def heap_sort(A):
    pass


def quick_sort(A):
    pass


def merge_sort(A):
    pass


def radix_sort(A):
    '''
        Radix sort can only be used if the data in the array are integers
        and non-negative numbers (unless modifications are made).

        Time-complexity: roughly O(n), can depend on the size of the numbers
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
    pass


if __name__ == "__main__":
    main()
