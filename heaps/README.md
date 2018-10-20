# Heaps

Heaps are a data structure that allow for easy manipulation of data. They can
be thought of as a tree structure, though they are typically stored in an array,
where for a root node `A[i]` its children are stored at `A[2*i]` and `A[2*i+1]`.

## Min-Heap vs. Max-Heap

The difference between a min- and max-heap is a slight nuance in the _heap property_.
For a min-heap, the heap property is for every root node, both of its children must
contain data that is less than the data of the root. In a max-heap, the property is
simply reversed, a root node must contain data that is more than the data in each of
its children.

## Heapify

Heapify is the procedure where for a subtree rooted at index i, the function recurses
down until the heap property is satisfied for all nodes it is called on. The run time
of heapify is O(h) where h is the height of the tree. This is approximately O(lgn).

## Build-Heap

To build a heap, simply start with any plain array. For convenience, heaps in an array
should be 1-indexed instead of 0-indexed. This is to allow the children for a node `i`
to be at indices `i*2` and `i*2+1`. After adjusting the array, call heapify from `A[n/2]`
to `A[1]`. These nodes are the only possible nodes that can have children, so calling heapify
on these nodes assures that the heap property is satisfied for all nodes that have children.
The runtime of build-heap intuitively would be O(nlgn) because there are O(n) calls to
heapify which is O(lgn). However, this is not the tightest upper boundary. Because the
heapify call is dependent on the height of the tree h, as O(h), it can be shown that a
tighter boundary of O(n) holds.

## Heap-Insert

To insert into a heap, add the element to the end of the array, then swap the new element
with the root of the heap. Finally, call `heapify()` on the root. This will ensure the heap
property is satisfied for the entire heap. Since there is only one call to heapify, the
runtime of inserting is O(h) where h is the height of the tree. This is approximately
O(lgn).
