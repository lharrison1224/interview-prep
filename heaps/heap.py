'''
    This module contains code for basic heap operations. All references to
    a heap are assumed to be a max-heap.
'''


def main():

    heap = build_heap([10, 15, 3])
    print(heap)
    heap_insert(heap, 11)
    print(heap)
    print(heap_extract_max(heap))
    print(heap)
    print(heap_extract_max(heap))
    print(heap)


def heapify(A, i):
    left = 2*i
    right = 2*i+1
    largest = i
    heapsize = len(A) - 1  # subtract 1 because 1-indexed
    if left <= heapsize and A[left] > A[i]:
        largest = left

    if right <= heapsize and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)


def build_heap(A):
    # add 1 because our heaps are 1-indexed for convenience
    heap = [None] * (len(A) + 1)

    # copy the array into our heap structure
    for i in range(1, len(heap)):
        heap[i] = A[i-1]

    # call heapify for all nodes that have children
    for i in range(int((len(heap)-1)/2), 0, -1):
        heapify(heap, i)

    return heap


def heap_insert(A, key):
    A.append(key)

    i = len(A) - 1
    while i > 1 and A[i] > A[int(i/2)]:
        A[i], A[int(i/2)] = A[int(i/2)], A[i]
        i = int(i/2)


def heap_extract_max(A):
    A[1], A[len(A)-1] = A[len(A)-1], A[1]
    max_val = A.pop(len(A) - 1)
    heapify(A, 1)

    return max_val


if __name__ == "__main__":
    main()
