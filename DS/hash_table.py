"""Implement a hash table in Python.
Partnered with Elyanil, James Feore and Kurt Maurer
"""

from store_bst import BinTree


class HashTable(object):
    """Define a hash table and it's methods."""
    pass

    def __init__(self, size=None, hash_function=None):
        """Initialize a hash table."""
        if not size:
            size = 1024
        if not hash_function:
            hash_function = 'complex'

        if type(size) not in (float, int):
            raise TypeError("Size of hash must be positive integer >= 512.")
        elif size < 512:
            raise ValueError("Size must be >= 512.")
        else:
            self.table = [None] * size
        if hash_function == 'complex':
            self.hash_function = 1
        elif hash_function == 'naive':
            self.hash_function = 2
        else:
            raise ValueError("Specified hash must be either 'complex' or 'naive'.")

    def _naive_hash(self, key):
        """Additive hash function."""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value

    def _complex_hash(self, key):
        """One-at-a-time hash function."""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
            hash_value += (hash_value << 10)
            hash_value ^= (hash_value >> 6)
        hash_value += (hash_value << 3)
        hash_value ^= (hash_value >> 11)
        hash_value += (hash_value << 15)

        return hash_value

    def get(self, key):
        """Return the value associated with the key."""
        hash_value = self._hash(key)
        idx = hash_value % len(self.table)
        the_val = self.table[idx]
        if the_val:
            result = the_val.search(hash_value)
            if result:
                return result.store

    def set(self, key, val):
        """Store the value using the key."""
        hash_value = self._hash(key)
        idx = hash_value % len(self.table)
        if not self.table[idx]:
            tree = BinTree()
            tree.insert(hash_value, val)
            self.table[idx] = tree
        else:
            self.table[idx].insert(hash_value, val)

    def _hash(self, key):
        """Hash the provided key and return the hash."""
        if self.hash_function == 1:
            return self._complex_hash(key)
        else:
            return self._naive_hash(key)


if __name__ == '__main__':  # pragma: no cover
    poo = HashTable(hash_function='complex')
    print(poo.set("poop", "poop"))
    print(poo.set("soup", "soup"))
    print(poo.get("poop"))
    print(poo.get("soup"))
    # poo.get("poop")
