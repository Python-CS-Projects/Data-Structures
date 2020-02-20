
from dll_queue import Queue
from dll_stack import Stack
import sys
sys.path.append('./queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if is empty
        if self.value is None:
            # Initialize the tree
            self.value = BinarySearchTree(value)
        elif value >= self.value:
            if self.right is None:
                self.value = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.value = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # 1.Case bases
        # target found or none
        if self.value == target:
            return True
        elif self.right == target:
            return True
        elif self.left == target:
            return True
        else:
            self.contains(target)

            # 2. Recursive case
            # Go down lh or rh to find target

            # Return the maximum value found in the tree

    def get_max(self):
        # Higher values are to the rh
        # Could be recursive or a loop
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Calling function on current node
        cb(self.value)
        #lh is none / rh is none
        if self.left is None and self.right:
            cb(self.value)
        # 2. recursive by calling for_each(cb) on each side
        # Go left and right
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # Base case:
        # since we are not returning anthing we dont need a base case

    def iter_for_each(self, cb):
        # if is empty return 
        if self is None:
            return
        

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
