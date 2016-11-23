class Solution(object):
    def parse(self, s):
        ret = ""
        if s % 3 == 0:
            ret += "Fizz"
        if s % 5 == 0:
            ret += "Buzz"
        if not ret:
            return str(s)
        return ret
    
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [self.parse(i) for i in xrange(1,n+1)]