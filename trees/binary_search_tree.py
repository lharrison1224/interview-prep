class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def main():
    print("Creating root node of 5...")
    root = Node(5)
    print("Inserting 10...")
    bst_insert(root, 10)
    print("Inserting 15...")
    bst_insert(root, 15)
    print("Inserting 1...")
    bst_insert(root, 1)
    print("Inserting 3...")
    bst_insert(root, 3)
    print("Inserting 8...")
    bst_insert(root, 8)
    print("BST printed inorder")
    print_bst(root, mode="inorder")
    print("Searching tree for 11...")
    print("Found 11") if binary_search(root, 11) else print("Did not find 11")
    print("Searching tree for 5...")
    print("Found 5") if binary_search(root, 5) else print("Did not find 5")
    print("Deleting 5...")
    bst_delete(root, 5)
    print("Searching tree for 5...")
    print("Found 5") if binary_search(root, 5) else print("Did not find 5")
    print("BST printed inorder")
    print_bst(root, mode="inorder")
    print_bst(root, mode="breadth_first")


def bst_insert(root, val):
    if root is None:
        raise ValueError('Root node is None')

    if root.val == val:
        raise ValueError('Attempted to insert duplicate value into BST')

    if val < root.val:
        if root.left == None:
            root.left = Node(val)
        else:
            bst_insert(root.left, val)
    elif val > root.val:
        if root.right == None:
            root.right = Node(val)
        else:
            bst_insert(root.right, val)

    return root


def binary_search(root, val):
    if root is None:
        return False

    if root.val == val:
        return True

    if val < root.val:
        return binary_search(root.left, val)

    if val > root.val:
        return binary_search(root.right, val)


def print_bst(root, mode="inorder"):
    def inorder_print(root):
        if root is None:
            return

        inorder_print(root.left)
        print(root.val)
        inorder_print(root.right)

    def preorder_print(root):
        if root is None:
            return

        print(root.val)
        preorder_print(root.left)
        preorder_print(root.right)

    def postorder_print(root):
        if root is None:
            return

        postorder_print(root.left)
        postorder_print(root.right)
        print(root.val)

    def breadth_first_print(root):
        if root is None:
            return

        Q = [root]
        while len(Q) > 0:
            current = Q.pop(0)
            if current.left is not None:
                Q.append(current.left)
            if current.right is not None:
                Q.append(current.right)
            print(current.val)

    if mode == "inorder":
        inorder_print(root)

    elif mode == "preorder":
        preorder_print(root)

    elif mode == "postorder":
        postorder_print(root)

    elif mode == "breadth_first":
        breadth_first_print(root)


def bst_delete(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = bst_delete(root.left, val)

    elif val > root.val:
        root.right = bst_delete(root.right, val)

    # keys are the same, delete this
    else:

        # handles the case of node has 1 or 0 children
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # node has 2 children, find the biggest value in right subtree
        temp = root.right
        while temp.left is not None:
            temp = temp.left

        root.val = temp.val
        # delete the node we used to move up in the tree
        root.right = bst_delete(root.right, temp.val)

    return root


if __name__ == "__main__":
    main()
