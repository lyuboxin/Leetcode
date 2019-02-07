class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [-1] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.table[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.table[key] = -1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if self.table[key] == 1:
            return True
        else:
            return False

