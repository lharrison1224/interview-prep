'''
    This file contains the source code for heapsort, quicksort,
    merge sort, radix sort, and insertion sort.
'''

import math


def main():
    array = [1005, 100, 5, 87, 905, 1983, 1, 42, 314]

    # print("Radix sort")
    # radix_sort(array)

    # print("Insertion sort")
    # insertion_sort(array)

    # print("Merge sort")
    # merge_sort(array)

    print("Quick sort")
    quick_sort(array)

    print(array)


def heap_sort(A):
    pass


def quick_sort(A):
    '''
        Quick sort works by first partioning an array around a pivot such that all
        elements left of the pivot are less than equal to the pivot and all elements
        right of the pivot are greater than the pivot. Then the quick sort function
        is recursively called on both the left and right segments. 

        Quick sort is generally considered the best all-purpose sorting algorithm
        except in a few cases (integers only, linked lists)

        Time complexity (average/best cases): O(nlogn)
        Time complexity (worst case): O(n^2) occurs when the pivot is picked as the
                                             largest or smallest element every time
        Space complexity: O(1) extra space
        Stable: no, can be modified to be made stable by comparing value AND initial index
    '''

    # partition splits the given subarray into 3 sections: a segment that
    # is all <= to a pivot, a pivot, and a segment that is all > than a pivot
    # and it returns the index of the pivot
    def partition(A, low, high):

        # pick a pivot, can be anything, here it is last element
        # runtimes can be improved by picking 3 values and picking median
        pivot = A[high]

        # the index of where elements smaller than the pivot will be placed
        i = low - 1

        for j in range(low, high):

            # see if the current element is lower than the pivot
            if A[j] <= pivot:

                # increase the index to insert into
                i += 1
                A[i], A[j] = A[j], A[i]

        # place the pivot in its spot
        A[i+1], A[high] = A[high], A[i+1]
        return i+1

    # create a helper function so the user does not have to call
    # the function with low and high params
    def quick_sort_helper(A, low, high):

        # see if we have a valid subarray
        if low < high:

            # select a pivot using partition algorithm
            pivot = partition(A, low, high)

            # quicksort both halves of the array
            quick_sort_helper(A, low, pivot-1)
            quick_sort_helper(A, pivot+1, high)

    # call our helper
    quick_sort_helper(A, 0, len(A)-1)


def merge_sort(A):
    '''
        Merge sort works by splitting the array in half, calling merge
        sort on each half, then merging the two arrays together in order.

        Merge sort is better than quicksort if you are sorting a linked list
        because the merge operation can be done in O(1) space instead of O(n).
        In addition, it also has less "direct accesses" into an array, of the 
        form A[4]. As a linked list this is an expensive operation, and quicksort
        has a lot of these accesses.

        Time complexity: O(nlogn) ... actually theta(nlogn)
        Space complexity: O(n)
        Stable: yes
    '''

    # define a merge sort helper function to provide an interface to
    # the user that doesn't require them to provide a left and right index
    def merge_sort_helper(A, l, r):

        # check to see if the right index is larger than the left
        # because we are only concerned w/ arrays w/ at least 2 elements
        if l < r:

            # find the middle index
            middle = int((l+r)/2)

            # call merge sort on the left half
            merge_sort_helper(A, l, middle)

            # call merge sort on the right half
            merge_sort_helper(A, middle+1, r)

            # merge the two halves that were just sorted
            merge(A, l, middle, r)

    def merge(A, l, m, r):

        # count the elements in each side of the array
        nl = m - l + 1
        nr = r - m

        # create temp arrays
        L = [0] * (nl)
        R = [0] * (nr)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, nl):
            L[i] = A[l + i]

        for j in range(0, nr):
            R[j] = A[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray

        while i < nl and j < nr:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < nl:
            A[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < nr:
            A[k] = R[j]
            j += 1
            k += 1

    # call our helper
    merge_sort_helper(A, 0, len(A)-1)


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


if __name__ == "__main__":
    main()
