"""Implementation of a Deque via Nick Hunt-Walker.

append(val): adds value to the end of the deque
appendleft(val): adds a value to the front of the deque
pop(): removes a value from the end of the deque and returns it (raises an
    exception if the deque is empty)
popleft(): removes a value from the front of the deque and returns it (raises
    an exception if the deque is empty)
peek(): returns the next value that would be returned by pop but leaves the
    value in the deque (returns None if the deque is empty)
peekleft(): returns the next value that would be returned by popleft but leaves
    the value in the deque (returns None if the deque is empty)
size(): returns the count of items in the queue (returns 0 if the queue is
    empty)
"""

from double_linked_list import DLinkedList


class Deque(object):
    """A Double-Ended Queue."""

    def __init__(self):
        """Initialize a new double-ended queue."""
        self._container = DLinkedList()
        self._resize()

    def append(self, val):
        """Add to the tail of the Deque."""
        self._container.append(val)
        self._resize()

    def appendleft(self, val):
        """Add to the head of the Deque."""
        self._container.push(val)
        self._resize()

    def pop(self):
        """Remove and return from the tail of the Deque."""
        try:
            popped = self._container.shift()
            self._resize()
            return popped
        except IndexError:
            raise IndexError("Deque is empty.")

    def popleft(self):
        """Remove and return from the head of the Deque."""
        try:
            popped = self._container.pop()
            self._resize()
            return popped
        except IndexError:
            raise IndexError("Deque is empty.")

    def peek(self):
        """Look at the tail of the Deque."""
        return self._tail

    def peekleft(self):
        """Look at the head of the Deque."""
        return self._head

    def size(self):
        """Return the size of the Deque."""
        return self._size

    def _resize(self):
        self._head = self._container.head
        self._tail = self._container.tail
        self._size = self._container._size
