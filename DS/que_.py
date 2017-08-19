"""Implementation of a Queue via Nick Hunt-Walker.

enqueue(value): adds value to the queue
dequeue(): removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)
peek(): returns the next value in the queue without dequeueing it. If the queue
    is empty, returns None
size(): return the size of the queue. Should return 0 if the queue is empty.
"""
from double_linked_list import DLinkedList


class Queue(object):
    """A Queue object."""

    def __init__(self, iterable=None):
        """Initialize a new Queue object."""
        self._container = DLinkedList(iterable)
        self.resize()

    def enqueue(self, val):
        """Add a value to the tail of the Queue."""
        self._container.push(val)
        self.resize()

    def dequeue(self):
        """Remove a value from the head of the Queue."""
        try:
            shifted = self._container.shift()
        except IndexError:
            raise IndexError("Queue is empty.")
        self.resize()
        return shifted

    def peek(self):
        """Look at the next value in the Queue."""
        return self.head

    def size(self):
        """Return the size of the Queue."""
        return self._size

    def resize(self):
        """Re-assign the head, tail, and recalculate Queue size."""
        self.head = self._container.tail
        self.tail = self._container.head
        self._size = self._container.size()

    def __len__(self):
        """The length of the Queue."""
        return self.size()
