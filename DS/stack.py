"""Implementation of a Stack.

push(value) - Adds a value to the stack. The parameter is the value to be added
to the stack.
pop() - Removes a value from the stack and returns that value. If the stack is
empty, attempts to call pop should raise an appropriate Python exception class.
"""

from linked_list import LinkedList


class Stack(object):
    """A container with abilities to push and pop data."""

    def __init__(self, iterable=None):
        """Create a new stack."""
        self._container = LinkedList(iterable)
        self._resize()
        self.head = self._container.head

    def push(self, val):
        """Add a new value to top of the stack."""
        self._container.push(val)
        self._resize()
        self.head = self._container.head

    def pop(self):
        """Remove the value at the stop of the stack."""
        popped = self._container.pop()
        self._resize()
        self.head = self._container.head
        return popped.data

    def _resize(self):
        self.head = self._container.head
        self.size = self._container.size()

    def __len__(self):
        return self._container.size()
