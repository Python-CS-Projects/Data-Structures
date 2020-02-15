"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.length > 0:
            # Insert to the prev of the current head
            self.head.insert_before(value)
            # set the head as the new prev of the old head
            self.head = self.head.prev
            # increment count
            self.length += 1
        else:
            # create new node as the head
            self.head = ListNode(value)
            # and set the tail = to head
            self.tail = self.head
            # increment count
            self.length += 1

    def remove_from_head(self):
        if self.length > 0:
            to_delete = self.head.value
            self.delete(self.head)
            return to_delete
        else:
            return

    def add_to_tail(self, value):
        if self.length > 0:
            # insert after the current tail
            self.tail.insert_after(value)
            # now set the tail as the new next of the old tail
            self.tail = self.tail.next
            self.length += 1
        else:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1

    def remove_from_tail(self):
        if self.length > 0:
            delete = self.head.value
            self.delete(self.tail)
            return delete
        else:
            return

    def move_to_front(self, node):
        if node is not self.head:
            self.delete(node)
            self.add_to_head(node.value)

    def move_to_end(self, node):
        if node is not self.tail:
            self.delete(node)
            self.add_to_tail(node.value)

    def delete(self, node):
        # if is empty return because there is nothing to delete
        if self.length == 0:
            return
        # if the list has only one element
        elif self.head == self.tail:
            # delete by setting its tail or head = None
            self.tail = None
            self.head = None
        # if node.prev == None its the head
        elif node.prev == None:
            # since the node is the head we set the new head to the node next
            self.head = node.next
        # if node.next == None node is the tail
        elif node.next == None:
            # Since the node is the tail then set the new tail to the prev of the node
            self.tail = node.prev
        # Lastly if the node does not fall into any of the if, is some where in the middle
        # so we call delete which will rearrange the prev or next of the surranding nodes
        node.delete()
        self.length -= 1

    def get_max(self):
        pass
