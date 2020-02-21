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
        # if the key is in the dic move it to the end
        if key in self.storage:
            node = self.storage[key]
        # move value to the tail as recently used
            self.order.move_to_end(node)
            return node.value
        # else return none because the ley was not found
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
        # if the key already exist
        if key in self.storage:
            # get the value
            node = self.storage[key]
            # overwrite the value with the new value
            node.value = value
            # now we move it to the end as the most recent
            self.order.move_to_end(node)
        # if the key does not yet exist in the storage
        else:
            # if the lenght of the diccionary is equal to the limit 10
            if len(self.order) == self.limit:
                # here we iterate over the diccionary
                for name in self.storage:
                    # Find the value in the DLL
                    if self.storage[name] is self.order.head:
                        # Delete current head from Diccionary/Storage
                        del self.storage[name]
                        # Terminate
                        break
                # Delete the head from the DLL
                self.order.remove_from_head()
            # If the dic/storage is not yet full add the new value as most recent in the DLL
            self.order.add_to_tail(value)
            # add to the dic/storage tail
            self.storage[key] = self.order.tail
