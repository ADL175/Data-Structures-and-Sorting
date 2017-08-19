
"""Helper data structures for Trie traversal, worked with Erik Enderlein on this."""


class Node(object):  #pragma no cover
    """A node for the list. Has a value, and points to another node."""

    def __init__(self, value, next_up):
        """Node set up."""
        self.value = value
        self.next = next_up


class LinkedList(object):
    """Contain methods for working with nodes pointing to each other."""

    def __init__(self, optional_values=None):  #pragma no cover
        """List set up."""
        self.head = None
        self.length = 0
        if isinstance(optional_values, (tuple, list)):
            for x in optional_values:
                self.push(x)

    def __len__(self):
        """Return Length of list."""
        return self.size()

    def __str__(self):  #pragma no cover
        """Print list."""
        return self.display()

    def push(self, value):
        """Add node with value to head of list."""
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self):
        """Remove node from head of list."""
        if self.length is 0:
            raise IndexError('List is empty.')
        popped = self.head
        self.head = self.head.next
        self.length -= 1
        return popped.value

    def size(self):
        """Return Length of list."""
        return self.length

    def search(self, val):
        """Return node with given value, else return none."""
        if self.length is 0:
            return None
        temp = self.head
        while temp.value is not val:
            temp = temp.next
            if temp is None:
                return None
        return temp

    def remove(self, node_to_be_removed):
        """Remove given node from list."""
        if isinstance(node_to_be_removed, Node):
            if self.head is node_to_be_removed:
                self.head = self.head.next
            else:
                current_node = self.head
                while current_node:
                    if current_node.next is node_to_be_removed:
                        self.length -= 1
                        current_node.next = current_node.next.next
                        break
                    current_node = current_node.next
                if current_node is None:
                    raise IndexError("Node not found.")
        else:
            raise TypeError("Not a Node.")

    def display(self):
        """Return tuple like string of list."""
        current_node = self.head
        the_list = []
        while current_node:
            the_list.append(current_node.value)
            current_node = current_node.next
        to_return = '('
        for i in range(len(the_list)):
            to_return += '{}, '.format(the_list[i])
        if len(to_return) > 1:
            to_return = to_return[:-2]
        to_return += ')'
        return to_return


class Stack(object):
    """Ojbect inheretence from Linked list to create Stack Data structure."""

    def __init__(self, data=[]):
        """Instantiate new Stack."""
        self._new_linked_list = LinkedList(data)

    def pop(self):
        """Remove and returns node from top of the stack."""
        return self._new_linked_list.pop()

    def push(self, val):
        """Add a new node to the top of stack."""
        return self._new_linked_list.push(val)

    def __len__(self):
        """Return length of stack."""
        return self._new_linked_list.__len__()
