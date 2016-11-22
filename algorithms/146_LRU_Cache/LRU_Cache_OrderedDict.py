from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
        except:
            value = -1
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        try:
            self.cache.pop(key)
        except:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

if __name__ == "__main__":
    x = LRUCache(5)
    x.set(2,1)
    x.set(4,1)
    x.set(5,2)
    x.set(3,4)
    print x.get(2)