"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        root = BSTNode(value)
        currentval = self.value
        newval = value
        # take the current value of our node (self.value)
        # compare to the new value we wwnat to insert
        if newval < currentval:
            if self.left is not None:
                self.left.insert(newval)
            else:
                self.left = root

        if newval >= currentval:
            if self.right is not None:
                self.right.insert(newval)
            else:
                self.right = root

        # if new value <=self.value
            # if self.left is already taken by a node
            # make that node call insert

            # set the left to the new node with the new value

        # if new value >= self.value
            # if self.right is already taken by a node
            # make that right node call  insert.
            # set the right child to the new node with new value

        # newnode=self.head
        # if newnode <= root:
        #     self.left=newnode
        #     root.insert(3)
        # if newnode >= root:
        #     self.right=newnode
        #     root.

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # we're still traversing this
        # if current self.value is target
        # return true
        # compare the target to the current val
        # if curr val >= than target
        # check the left subtree
        # if you cant go left, return false
        # current val is <target
        # check if right subtree, contains target
        # if you cant go right, return false

        found = False
        current_val = self.value
        if current_val is target:
            return True
        # compare the target to the current val
        if current_val >= target:
            # check the left subtree(self.left.contains(target))
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if val>=target
        if current_val < target:
            # check if right subtree contains target
            # if you cant go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    # * i do not understand this part.
    def for_each(self, fn):
        # call fn on current val.
        fn(self.value)
        # if you can go left, call for each on the left tree
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()
