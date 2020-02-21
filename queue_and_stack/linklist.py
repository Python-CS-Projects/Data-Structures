class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list (if head == NONE LL is empty)
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_head(self, value):
        # create new node with value
        new_node = Node(value)
        # Update pointer of new Node -> head
        new_node.set_next(self.head)

        # Insert into empty list
        if self.head is Node:
            # Mark new Node as "head" and "tail"
            self.head = new_node
            self.tail = new_node

        # insert in new list with 1+ Nodes
        else:
            # Mark new Node as "head"
            self.head = new_node

    def add_to_tail(self, value):
        # Create new Node with Value
        new_node = Node(value)
        # Update next pointer of old tail
        self.tail.set_next(new_node)

        if self.tail is Node:
            # Mark new node as head and tail
            self.head = new_node
            self.tail = new_node
        # insert in new list with 1+
        else:
            self.tail = new_node

    def remove_head(self):
        # remove from empty LL
        if self.head == None:
            return
            # remove from LL with 1 elements
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # General
        else:
            self.head = self.head.get_next()

            # STRETCH

    def insert_at(self, value, position):
        pass

    def contains(self, value):
        cur_node = self.head
        while(cur_node is not None):
            cur_node = cur_node.get_next()
