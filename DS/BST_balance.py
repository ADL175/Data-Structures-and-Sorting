"""Implement Binary Search Tree.
I worked with Elyanil Castro, Kurt Maurer and James Feore.
"""


class Node(object):
    """Implement a node for BST."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Instantiate a new BST."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinTree(object):
    """Implement a binary search tree."""

    def __init__(self, val=None):
        self._root = None
        self._size = 0
        if type(val) in [list, tuple]:
            for item in val:
                self.insert(item)
        elif val:
            raise ValueError('BST only takes list or tuple.')

    def insert(self, val):
        """Insert a value into the BST."""
        if type(val) not in [int, float]:
            raise ValueError('Please insert only integers or floats')
        if not self._root:
            self._root = Node(val)
            self._size += 1
        else:
            curr = self._root
            while curr:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        curr.right = Node(val, parent=curr)
                        self._size += 1
                        self.rebalance(curr)
                        return
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(val, parent=curr)
                        self._size += 1
                        self.rebalance(curr)
                        return
                else:
                    return

    def search(self, val):
        """Search a value in the BST."""
        if type(val) not in [int, float]:
            raise ValueError('BST is only made of numbers')
        if not self._root:
            return None
        else:
            curr = self._root
            while curr:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        return None
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        return None
                elif val == curr.val:
                    return curr

    def contains(self, val):
        """Check to see if the BST contains a value, returns Boolean."""
        return not not self.search(val)

    def size(self):
        """Returns total number of Nodes in BST."""
        return self._size

    def depth(self, node=None):
        """Find the depth of a specified Node."""
        if not node:
            node = self._root
            if not node:
                return 0
        l_depth = 0
        r_depth = 0

        if node.left:
            l_depth = self.depth(node.left)
        if node.right:
            r_depth = self.depth(node.right)

        if not node.left and not node.right:
            return 1
        elif l_depth >= r_depth:
            return l_depth + 1
        elif l_depth < r_depth:
            return r_depth + 1

    def balance(self, start=None):
        """Return an integer representing if the tree is balanced or not."""
        if self._root is None:
            return 0
        if not start:
            start = self._root

        l_depth = 0
        r_depth = 0
        if start.left:
            l_depth = self.depth(start.left)
        if start.right:
            r_depth = self.depth(start.right)
        return l_depth - r_depth

    def delete(self, val):
        """Delete a value from BST and re-order BST."""
        start = self.search(val)
        if start:
            is_root = True if start is self._root else False

            if not start.left and not start.right:  # if no children
                if is_root:
                    self._root = None
                else:
                    if start.parent.val > start.val:
                        start.parent.left = None
                    else:
                        start.parent.right = None
                    self.rebalance(start.parent)
            elif start.left and start.right:  # has two children
                if self.balance(start) < 0:
                    small = start.right
                    is_left = False
                    while small.left:
                        small = small.left
                        is_left = True
                    start.val = small.val
                    if is_left:
                        small.parent.left = small.right
                        if small.right:
                            small.right.parent = small.parent
                    else:
                        start.right = small.right
                        if small.right:
                            small.right.parent = start
                    self.rebalance(small)
                else:
                    small = start.left
                    is_right = False
                    while small.right:
                        small = small.right
                        is_right = True
                    start.val = small.val
                    if is_right:
                        small.parent.right = small.left
                        if small.left:
                            small.left.parent = small.parent
                    else:
                        start.left = small.left
                        if small.left:
                            small.left.parent = start
                    self.rebalance(small)
            elif start.left:
                start.val = start.left.val
                tmp_r = start.left.right
                tmp_l = start.left.left
                start.right = tmp_r
                start.left = tmp_l
                self.rebalance(start)
            elif start.right:
                smart.val = start.right.val
                tmp_r = start.right.right
                tmp_l = start.right.left
                start.right = tmp_r
                start.left = tmp_l
                self.rebalance(start)
            self._size -= 1
        return None

    def rebalance(self, start):
        while start:
            direction = self.balance(start)
            if direction > 1:
                if self.balance(start.left) < 0:
                    start = self.rotate_rightleft(start)
                else:
                    start = self.rotate_right(start)
            elif direction < -1:
                if self.balance(start.right) > 0:
                    start = self.rotate_leftright(start)
                else:
                    start = self.rotate_left(start)
            else:
                start = start.parent
        return None

    def rotate_left(self, start):
        """Rotate the tree extending from the start to the left."""
        rotate_to = start.right
        if start is self._root:
            self._root = rotate_to
        rotate_to.parent = start.parent
        if start.parent:
            if start.parent.val < rotate_to.val:
                start.parent.right = rotate_to
            elif start.parent.val > rotate_to.val:
                start.parent.left = rotate_to
        start.parent = rotate_to
        start.right = rotate_to.left
        if rotate_to.left:
            rotate_to.left.parent = start
        rotate_to.left = start
        start = start.parent
        return start

    def rotate_leftright(self, start):
        """Rotate tree extending from start to left-right."""
        rotate_to = start.right.left
        if start is self._root:
            self._root = rotate_to
        temp_right = start.right.left.right
        temp_left = start.right.left.left
        rotate_to.right = rotate_to.parent
        rotate_to.parent = start.parent
        if start.parent:
            if start.parent.val < rotate_to.val:
                start.parent.right = rotate_to
            elif start.parent.val > rotate_to.val:
                start.parent.left = rotate_to
        start.parent = rotate_to
        rotate_to.left = start
        rotate_to.right.parent = rotate_to
        rotate_to.left.right = temp_left
        rotate_to.right.left = temp_right
        start = start.parent
        return start

    def rotate_right(self, start):
        """Rotate the tree extending from the start to the right."""
        rotate_to = start.left
        if start is self._root:
            self._root = rotate_to
        rotate_to.parent = start.parent
        if start.parent:
            if start.parent.val < rotate_to.val:
                start.parent.right = rotate_to
            elif start.parent.val > rotate_to.val:
                start.parent.left = rotate_to
        start.parent = rotate_to
        start.left = rotate_to.right
        if rotate_to.right:
            rotate_to.right.parent = start
        rotate_to.right = start
        start = start.parent
        return start

    def rotate_rightleft(self, start):
        """Rotate tree extedning from the start to the right-left."""
        rotate_to = start.left.right
        if start is self._root:
            self._root = rotate_to
        temp_left = start.left.right.left
        temp_right = start.left.right.right
        rotate_to.left = rotate_to.parent
        rotate_to.parent = start.parent
        if start.parent:
            if start.parent.val < rotate_to.val:
                start.parent.right = rotate_to
            elif start.parent.val > rotate_to.val:
                start.parent.left = rotate_to
        start.parent = rotate_to
        rotate_to.right = start
        rotate_to.left.parent = rotate_to
        rotate_to.right.left = temp_right
        rotate_to.left.right = temp_left
        start = start.parent
        return start

    def in_order(self, node=None):
        """Traverse the list in order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.in_order(node.left):
                yield each_val
        yield node.val
        if node.right:
            for each_val in self.in_order(node.right):
                yield each_val

    def pre_order(self, node=None):
        """Traverse the list in pre_order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        yield node.val
        if node.left:
            for each_val in self.pre_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.pre_order(node.right):
                yield each_val

    def post_order(self, node=None):
        """Traverse the list in post_order."""
        if node and not isinstance(node, Node):
            raise TypeError('Traversal only accepts None or Node as params')
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.post_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.post_order(node.right):
                yield each_val
        yield node.val

    def breadth_first(self):
        """Peform BFT on the BST."""
        if not self._root.val:
            yield None
        yield self._root.val
        traverse = []
        if self._root.left:
            traverse.append(self._root.left)
        if self._root.right:
            traverse.append(self._root.right)
        while traverse:
            curr = traverse[0]
            yield curr.val
            if curr.left:
                traverse.append(curr.left)
            if curr.right:
                traverse.append(curr.right)
            traverse.remove(curr)

#
# if __name__ == '__main__':  # pragma: no cover
#     import timeit
#     setup = "'"
#
# from bst import BinTree
# binary_search = BinTree([5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11])
# binary_search.search({})
# '''
#     pre_bst = [5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11]
#     search_num = input('''
# The following values are contained in a binary search tree:
#
# [5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11]
#
# Enter a number to check the performance of the search function.
# >>> ''')
#     while isinstance(search_num, str):
#         try:
#             search_num = int(search_num)
#         except ValueError:
#             search_num = input("Integer, please.")
#     new_setup = setup.format(search_num)
#     times = timeit.repeat(new_setup, number=100, repeat=10)
#     print('''
# Searched binary search tree for the number {} function 100 times, repeated 10 times.
# Best: {}s
# Worst: {}s'''.format(search_num, min(times), max(times)))
