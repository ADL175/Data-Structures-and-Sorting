"""Binary Search Tree implementation via Nick Hunt-Walker."""

from que import Queue
from stack import Stack


class Node(object):
    """A Node object for use with the Binary Search Tree structure."""

    def __init__(self, value=None, parent=None, left=None, right=None):
        """Initialize a new BST node."""
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

    def has_child(self):
        """Returns whether or not this node has a child."""
        return self.left is not None or self.right is not None

    def __repr__(self):
        return str(self.value)


class BinarySearchTree(object):
    """A Binary Search Tree structure."""

    def __init__(self, iterable=None):
        """Initialize a new BST structure."""
        self._size = 0
        self._root = None
        self._depth = 0

        if iterable:
            if hasattr(iterable, "__iter__") or isinstance(iterable, str):
                for val in iterable:
                    self.insert(val)

    def insert(self, val):
        """Add a new node to the tree."""
        new_node = Node(val)
        if not self._root:
            self._root = new_node
            self._size += 1
            self._depth += 1

        else:
            curr = self._root
            potential_depth = 0
            while curr:
                if val < curr.value:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new_node
                        new_node.parent = curr
                        self._size += 1

                elif val > curr.value:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        new_node.parent = curr
                        self._size += 1

                else:
                    break

                potential_depth += 1
            if potential_depth > self._depth:
                self._depth = potential_depth

    def contains(self, val):
        """Return whether or not the tree contains this value."""
        return True if self._search(val) else False

    def size(self):
        """Return the total number of nodes in the tree."""
        return self._size

    def depth(self):
        """Return the maximum depth of the tree."""
        return self._depth

    def balance(self):
        """Return the numerical balance of the tree.

        (-) the tree is deeper on the left than the right.
        (+) the tree is deeper on the right than the left.
        """
        if not self._root:
            return 0
        return self._check_balance(self._root)

    def breadth_first_traversal(self):
        """A breadth-first traversal generator for the BST."""
        queue = Queue()
        node = self._root
        while node:
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            yield node.value
            try:
                node = queue.dequeue().data
            except IndexError:
                raise StopIteration

    def pre_order_traversal(self):
        """The pre-order depth-first traversal."""
        stack = Stack()
        node = self._root
        stack.push(node)
        while node:
            try:
                node = stack.pop()
                yield node.value
                if node.right:
                    stack.push(node.right)
                if node.left:
                    stack.push(node.left)
            except IndexError:
                raise StopIteration

    def in_order_traversal(self):
        """The in-order depth-first traversal."""
        stack = Stack()
        visited = []
        node = self._root
        while node:
            if node not in visited:
                stack.push(node)
            if node.left and node.left not in visited:
                node = node.left
                continue
            else:
                yield node.value
                try:
                    visited.append(stack.pop())
                except IndexError:
                    raise StopIteration
            if node.right and node.right not in visited:
                node = node.right
            else:
                try:
                    node = stack.pop()
                except IndexError:
                    raise StopIteration

    def post_order_traversal(self):
        """The post-order depth-first traversal."""
        stack = Stack()
        visited = []
        node = self._root
        while node:
            if node not in visited:
                stack.push(node)
            if node.left and node.left not in visited:
                node = node.left
                continue
            if node.right and node.right not in visited:
                node = node.right
                continue
            yield node.value
            try:
                visited.append(stack.pop())
                node = stack.pop()
            except IndexError:
                raise StopIteration

    def delete(self, val):
        """Delete this node from the tree."""
        node = self._search(val)
        if node:
            # if it has no kids, just remove it.
            self._size -= 1
            parent = node.parent
            if not node.has_child():
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self._root = None

            elif node.left and not node.right:
                # if left
                if parent:
                    if node == parent.left:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    self._root = node.left

            elif node.right and not node.left:
                # if right
                if parent:
                    if node == parent.left:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                else:
                    self._root = node.right

            else:
                # both children. get right child's left-most node
                min_node = self._get_min(node)
                if not parent:
                    min_node.left = node.left
                    if node.right == min_node:
                        node.right.parent = None
                    else:
                        if min_node.right:
                            min_node.parent.left = min_node.right
                        else:
                            min_node.parent.left = None
                        min_node.right = node.right
                        node.right.parent = min_node

                    node.left.parent = min_node

                    self._root = min_node
                    self._root.parent = None

                else:
                    if node.right == min_node:
                        min_node.right = min_node.right if min_node.right else None
                    else:
                        min_node.right = node.right

                    min_node.left = node.left

                    if node == node.parent.left:
                        node.parent.left = min_node
                    elif node == node.parent.right:
                        node.parent.right = min_node
                    min_node.parent = parent

            node.parent = None

    def _get_min(self, node):
        """Return the node's right child's left-most node."""
        node = node.right
        while node.left:
            node = node.left
        return node

    def _search(self, val):
        """Search for the node that contains the value."""
        curr = self._root
        while curr:
            if val == curr.value:
                return curr
            elif val < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    return False
            else:
                if curr.right:
                    curr = curr.right
                else:
                    return False

    def _check_balance(self, node):
        """Check the balance of a subtree given a root node."""
        # recurse down left side until hit bottom
        if not node.left and not node.right:
            return 0

        if node.left and not node.right:
            return self._check_balance(node.left) - 1

        if node.right and not node.left:
            return self._check_balance(node.right) + 1

        left = self._check_balance(node.left)
        right = self._check_balance(node.right)
        return left + right

    def __len__(self):
        """Return the size of the tree, compatible with len() function."""
        return self.size()
