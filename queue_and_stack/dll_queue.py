# from doubly_linked_list import DoublyLinkedList
import linklist
import sys
# sys.path.append('../doubly_linked_list')
sys.path.append('./linklist.py')

# Initialize linklist
link = linklist.LinkedList()


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        link.add_to_tail(value)

    def dequeue(self):
        self.size -= 1
        link.remove_head()

    def len(self):
        return self.size
