# Hash Tables

Most commonly, hash tables are found in integral parts of languages in the form of either maps or dictionaries.

## Hash Functions

In order to implement a hash table, one needs to define a _hash function_. A hash function is a defined set of mathematical
operations that are performed on a given key, which is commonly a string. Common choices for hash functions are either linear
or quadratic.

```python
    # linear
    total = 0
    for char in string:
        total += 5 * ord(char)
    hash_value = total % TABLE_SIZE
```

```python
    # quadratic
    total = 0
    for char in string:
        total += ord(char) ** 2
    hash_value = total % TABLE_SIZE
```

### Important Characteristics

- **Deterministic**: Hash functions should always return the same value for the same string input
- **Spread**: Hash functions should evenly spread outputs over the interval [0, TABLE_SIZE-1], this is important especially for _open-addressing_
- **Unique Values**: Hash functions should attempt to return an even number of keys for any given value in the range [0, TABLE_SIZE-1]

## Collision Handling

A _collision_ occurs when two values have the same hash value. Since the backing data structure for a hash table is an array, we cannot place multiple values
at the same array index. There are two common methods to handle this.

### Chaining

In chaining, the backing array is actually a pointer to a linked list containing all elements with that given hash value.
As a new value comes in, if the array index corresponding to its hash value contains `null`, the new element is allocated and its address is put into the array at the index.
If the array at the index is not `null`, you simply append the new element to the end of the linked list at that location.
To perform a lookup, one hashes the given key, goes to that index in the array, and if the array is `null` there, then return `False` or `null`. If the array index is not `null`, the array contents at that index are a pointer to the head of a linked list that _will_ contain the element _if_ it exists in the table. From there, simply iterate through the linked list and check for a key match.

### Open-Addressing

In open-addressing, the backing array contains the actual data. As a new value comes in, one hashes the given key, then looks at that index in the array. If that given index is empty, simply place the value at that index. However, if the index is filled, iterate to the next index in the array and repeat until an empty index is found.
Once an empty index is found, simply place the value there.
To perform a lookup, hash the given key, and look at the array at that given index. If the index is empty, the value is not found, return `False` or `null`. If there is a value at the location, check for a key match. If not a key match, iterate to the next consecutive index and check for a key match. Repeat this process until a key match or an empty index is found. If an empty index is found, the key was not found.

#### Tombstoning

In open-addressing, extra action must be taken if one wants to remove a value. If the value is removed, a _tombstone_, a simple marker that represents a space that was at one time filled, must be placed at that index. As one iterates through the array after a collision, if a tombstone is reached, the search continues for a key match. Without a tombstone, the search would stop at that index, even though the actual key could exist at a later index.

### Common Languages

Languages that use chaining

- Java
- Scala
- Go

Languages that use open-addressing

- Python
- Ruby
- C++
