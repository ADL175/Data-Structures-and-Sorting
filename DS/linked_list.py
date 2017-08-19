"""Implementation of a Singly-Linked List via Nick Hunt-Walker."""

# In that module, write the required Python class(es) to implement a
# linked list. The list class should be named LinkedList. Your list
# implementation should support the following methods:

# push(val) will insert the value ‘val’ at the head of the list
# pop() will pop the first value off the head of the list and return it.
# size() will return the length of the list
# search(val) will return the node containing ‘val’ in the list, if present,
# else None
#
# remove(node) will remove the given node from the list, wherever it might be
# (node must be an item in the list)
#
# display() will return a unicode string representing the list as if it were a
# Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
#
# The constructor for your LinkedList class should allow optionally
# passing an iterable of values. If an iterable is provided, the result
# will be a linked list instance containing the values in the iterable.
# The head of the list should be the last item in the iterable:


class Node(object):
    """A node object for holding data and pointing at other nodes."""

    def __init__(self, data=None, next_node=None):
        """Take in a value and a next node."""
        self.data = data
        self.next = next_node


class LinkedList(object):
    """A singly linked list setting pointers to nodes."""

    def __init__(self, iterable=None):
        """Construct the linked list object."""
        self.head = None
        self._size = 0

        if iterable:
            if hasattr(iterable, "__iter__"):
                for value in iterable:
                    self.push(value)

            else:
                raise TypeError("You did not provide an iterable.")

    def push(self, val):
        """Insert a value at the head of the list."""
        self.head = Node(val, self.head)
        self._size += 1

    def pop(self):
        """Remove and return the node at the head of the list."""
        popped = self.head
        if not popped:
            raise IndexError("The list is empty.")
        self.head = self.head.next
        self._size -= 1
        popped.next = None
        return popped

    def size(self):
        """Return the length of the list."""
        return self._size

    def search(self, val):
        """Return the node containing the given value if exists."""
        next_node = self.head
        while next_node:
            if next_node.data == val:
                return next_node
            else:
                next_node = next_node.next

        return None

    def remove(self, node):
        """Remove the given node from the list if exists."""
        prev_node = None
        to_remove = self.head

        if not node:
            raise ValueError("Node not in list")

        if self.head.data == node.data:
            self.head = self.head.next
            self._size -= 1
            return

        while to_remove:
            if to_remove.data == node.data:
                prev_node.next = to_remove.next
                self._size -= 1
                return

            else:
                prev_node = to_remove
                to_remove = to_remove.next

    def display(self):
        """Print the string representation of the list as tuple."""
        result_str = "("
        node = self.head
        while node:
            result_str += str(node.data)
            if node.next:
                result_str += ', '

            node = node.next

        result_str += ")"
        return result_str

    def __len__(self):
        """Allow built-in len function to return list size."""
        return self._size

    def __repr__(self):
        """String representation of this object."""
        return self.display()
