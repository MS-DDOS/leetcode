from collections import deque
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.LRU = deque()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.LRU.remove(key)
        self.LRU.appendleft(key)
        return self.cache[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.LRU.remove(key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.LRU.pop()]
        self.LRU.appendleft(key)
        self.cache[key] = value

if __name__ == "__main__":
    x = LRUCache(5)
    x.set(2,1)
    x.set(4,1)
    x.set(5,2)
    x.set(3,4)
    print x.get(2)