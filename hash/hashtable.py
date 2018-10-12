'''
    This file contains source code for constructing hash tables
    from simple arrays (or lists in this case)
'''
# the number of "buckets" in the hash table, typically a prime number
NUM_BUCKETS = 13

'''
    Say we want to build an application that allows users to see if a certain 
    student is enrolled in a class. To do this efficiently for large N, we want
    to build a hash table.
'''


def main():

    students = ["Jimmy", "Logan", "Hayden", "Katie", "Ashley", "Skylar",
                "Chris", "Dalton", "Kim", "Mark", "Bill", "Madison", "Claire"]

    # declare an empty list to serve as the hash table
    # the hash table needs NUM_BUCKETS of empty lists inside
    hash_table = [[] for _ in range(NUM_BUCKETS)]

    for student in students:

        # add the student to the hash table
        hash_table[hash_function(student)].append(student)

    # get the name that the user wants to search for
    requested_name = input(
        "Enter the name of the student you wish to search for: ")

    # to look up a student in the hashtable, we hash the requested name, then
    # iterate through the list of all students in that bucket to see if it
    # matches the name
    student_found = False
    for possible_match in hash_table[hash_function(requested_name)]:

        # see if the names match
        if possible_match == requested_name:
            print("Student found! {} is enrolled in the class".format(requested_name))
            student_found = True
            break

    if not student_found:
        print("Student not found. {} is not enrolled in the class".format(
            requested_name))


'''
    Hash functions are the novel idea behind hash tables. Essentially, a
    hash function takes a key (almost always a string), performs some
    mathematical operation on it, and returns an index that represents
    the "bucket" that the element should be placed into. It is paramount
    that a hash function is well-defined and deterministic.
'''


def hash_function(key):

    # simple loop variables
    counter = 0
    total = 0

    # loop through the characters in the string
    for char in key:
        # take the numerical value of the character and mult by counter^2
        # and add it to a running total
        total += ord(char) * (counter**2)
        counter += 1

    # use the total to get a number between 0 and num_buckets-1
    return total % NUM_BUCKETS


if __name__ == "__main__":
    main()
