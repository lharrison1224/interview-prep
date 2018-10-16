'''
    This module contains code for basic heap operations. All references to
    a heap are assumed to be a max-heap.
'''


def main():

    build_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def heapify():
    pass


def build_heap(A):
    # add 1 because our heaps are 1-indexed for convenience
    heap = [0] * (len(A) + 1)

    # copy the array into our heap structure
    for i in range(1, len(heap)):
        heap[i] = A[i-1]

    # call heapify for all nodes that have children
    for i in range(int((len(heap)-1)/2), 0, -1):
        print(i)
        # heapify(heap, i)


def heap_insert():
    pass


def heap_extract_max():
    pass


if __name__ == "__main__":
    main()
