
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
        # base case, is given value is none return
        if value is None:
            return
        # base case, if the tree is empty insert at first position
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # if is less than parent value go left
        elif self.value > value:
            # if left is None there is nothing on the left inset there
            if self.left is None:
                # assign tree to left
                self.left = BinarySearchTree(value)
            # else we recurese until we find the correct position rh/lh
            else:
                # we use recursion on the specific left value to keep going down
                self.left.insert(value)
        # if is greater than parent value we go right
        elif self.value <= value:
            # if  right is None (default)
            if self.right is None:
                # assign tree to right
                self.right = BinarySearchTree(value)
            else:
                # assess right tree and recurse
                self.right.insert(value)

   # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if tree is empty return
        if self.value is None:
            return
        # if the value equal the target return true
        elif self.value == target:
            return True
        # else we have to go down the tree
        else:
            # Check if there is a value on both sides
            if self.left is not None and self.right is not None:
                # IF there is a value we recurse over the values
                return self.left.contains(target) or self.right.contains(target)
            # if there is a value on the lh but not on rh
            elif self.left is not None:
                # Recurse only on that side
                return self.left.contains(target)
            # if there is a value only on the right side then recurse on the side
            elif self.right is not None:
                return self.right.contains(target)
            # If the is no value on either side then return
            else:
                return

    # Return the maximum value found in the tree
    def get_max(self):
        # The highest will always be right
        # Check if there right is None if so then we return current top value
        if self.right is None:
            return self.value
        # if right is not Not then we recurse to keep goint down
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if the value is None the is empty and we terminate by returning
        if self.value == None:
            return
        # else we call cb on the value
        else:
            cb(self.value)

            # if there is a value on both sides
            if self.left is not None and self.right is not None:
                # we recurse on both sides
                return self.left.for_each(cb), self.right.for_each(cb)
            # IF only lh has a velue
            elif self.left is not None:
                # recurse over that side
                return self.left.for_each(cb)
            # if only right has a value
            elif self.right is not None:
                # recurse over that side
                return self.right.for_each(cb)
            # if neither side has a value return
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
