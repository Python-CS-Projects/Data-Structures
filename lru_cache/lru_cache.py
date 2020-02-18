from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # UPDATE THE POSITION OF THE RECENTLY GET OR RECENTLY USE KEY
    # SO THE RECENTLY USE GOES TO ??

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
        # move value to the tail as recently used
            self.order.move_to_front(node)
            return node
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # IF THE CACHE IS FULL THE NEW VALUE TAKE PLACE OF THE OLDEST VALUE
    # THE OLDEST GOES TO ?? WHICH CAN POTENTIALLY BE OVERWRITTEN IF NO SPACE

    def set(self, key, value):
        if key in self.storage.keys():
            self.order.move_to_front(value)

        # if not full add to tail and substract from limit 10
        elif self.size < self.limit:

            self.order.add_to_head(value)
            self.storage[key] = self.order.head
            self.size += 1
         # if the chache is full remove from head and add value to tail
        else:
            self.storage[key] = value
            self.order.remove_from_tail()
            self.order.add_to_head(value)
