u"""Implementation of a doubly-linked list via Nick Hunt-Walker.

push(val) will insert the value ‘val’ at the head of the list
append(val) will append the value ‘val’ at the tail of the list
pop() will pop the first value off the head of the list and return it.
shift() will remove the last value from the tail of the list and return it.
remove(val) will remove the first instance of ‘val’ found in the list, starting
    from the head. If ‘val’ is not present, it will raise an appropriate
    Python exception.

"""

from linked_list import LinkedList, Node


class DNode(Node):
    """A double-ended Node object."""

    def __init__(self, data=None, prev_node=None, next_node=None):
        """Take in a value and a next node."""
        super(DNode, self).__init__(data, next_node)
        self.prev = prev_node


class DLinkedList(LinkedList):
    """A double-linked list object."""

    def __init__(self, iterable=None):
        """Initialize the double-linked list."""
        self.tail = None
        super(DLinkedList, self).__init__(iterable)

    def push(self, val):
        """Add a new value to the head of the list."""
        self.head = DNode(val, None, self.head)

        if not self.head.next:
            self.tail = self.head

        elif not self.head.next.next:
            self.tail.prev = self.head

        elif not self.head.next.prev:
            self.head.next.prev = self.head

        self._size += 1

    def append(self, val):
        """Add a new value to the tail of the list."""
        self.tail = DNode(val, self.tail, None)

        if not self.tail.prev:
            self.head = self.tail

        elif not self.tail.prev.prev:
            self.head.next = self.tail

        elif not self.tail.prev.next:
            self.tail.prev.next = self.tail

        self._size += 1

    def pop(self):
        """Remove and return the value at the head of the list."""
        popped = super(DLinkedList, self).pop()
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None

        return popped

    def shift(self):
        """Remove and return the value at the tail of the list."""
        if self.size() == 0:
            raise IndexError("The list is empty.")
        shifted = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self._size -= 1
        shifted.prev = None
        return shifted

    def remove(self, node):
        """Remove the given node from the list if exists."""
        prev_node = None
        to_remove = self.head

        if not node:
            raise ValueError("Node not in list")

        if self.head.data == node.data:
            self.head = self.head.next
            self.head.prev = None
            self._size -= 1
            return

        while to_remove:
            if to_remove.data == node.data:
                prev_node.next = to_remove.next
                to_remove.next.prev = prev_node
                self._size -= 1
                return

            else:
                prev_node = to_remove
                to_remove = to_remove.next
