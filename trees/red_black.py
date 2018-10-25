'''
    This module contains source code for the implementation of
    red-black trees.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = "RED"


def main():
    root = rb_insert(None, 5)
    root = rb_insert(root, 7)
    root = rb_insert(root, 3)
    root = rb_insert(root, 4)
    inorder_print(root)


def rb_insert(root, val):

    def rb_insert_helper(root, val):
        if root is None:
            return Node(val)

        if root.val == val:
            raise ValueError('Attempted to insert duplicate value into BST')

        if val < root.val:
            root.left = rb_insert_helper(root.left, val)
        elif val > root.val:
            root.right = rb_insert_helper(root.right, val)

        return root

    def left_rotate(x):
        pass

    def right_rotate(x):
        pass

    def rb_fixup(root, val):
        # if the current node was the root
        if root.val == val:
            root.color = "BLACK"
            return root

        # need to check the "uncle" of the node
        parents = []
        tmp = root
        while tmp.val != val:
            parents.insert(0, tmp)
            if val < tmp.val:
                tmp = tmp.left
            else:
                tmp = tmp.right

        # now the parents list is a stack where the first element is the
        # parent of the node, the second is the grandparent

        # parent can never be None if we have made it this far
        parent = parents.pop(0)

        if parent.color == "BLACK":
            # if the color of the parent is black we haven't violated any properties
            return root

        # grandparent cannot be None either because the prior case will catch
        grandparent = parents.pop(0)
        uncle = grandparent.left if grandparent.left is not parent else grandparent.right

        if uncle.color is "RED":
            parent.color = "BLACK"
            uncle.color = "BLACK"
            grandparent.color = "RED"
            return rb_fixup(root, grandparent.val)
        else:
            pass

    root_after_insert = rb_insert_helper(root, val)
    return rb_fixup(root_after_insert, val)


def inorder_print(root):
    if root is None:
        return
    inorder_print(root.left)
    print(root.val, root.color)
    inorder_print(root.right)


if __name__ == '__main__':
    main()
