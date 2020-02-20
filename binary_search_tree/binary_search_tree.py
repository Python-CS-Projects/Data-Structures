
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
        print('insert', self.value)
        # base case
        if value is None:
            return
        # base case for vertices
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # if vertex is less than parent vertex value
        elif self.value > value:
            # if vertex left is None (default)
            if self.left is None:
                # assign tree to left
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if vertex is greater than parent vertex value
        elif self.value <= value:
            # if vertex right is None (default)
            if self.right is None:
                # assign tree to right
                self.right = BinarySearchTree(value)
            else:
                # assess right tree and recurse
                self.right.insert(value)
   # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value is None:
            return
        elif self.value == target:
            return True
        else:
            if self.left is not None and self.right is not None:
                return self.left.contains(target) or self.right.contains(target)
            elif self.left is not None:
                return self.left.contains(target)
            elif self.right is not None:
                return self.right.contains(target)
            else:
                return

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value == None:
            return
        else:
            cb(self.value)

            if self.left is not None and self.right is not None:
                return self.left.for_each(cb), self.right.for_each(cb)
            elif self.left is not None:
                return self.left.for_each(cb)
            elif self.right is not None:
                return self.right.for_each(cb)
            else:
                return

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
