class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        j = len(x)-1
        for i in xrange(len(x)):
            if x[i] != x[j]:
                return False
            j -= 1
        return True
