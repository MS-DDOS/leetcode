from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        repeats = {}
        indices = OrderedDict()
        for i in xrange(len(s)):
            if s[i] in indices:
                repeats[s[i]] = None
            else:
                indices[s[i]] = i
        if len(indices) == len(repeats):
            return -1
        else:
            for rep in repeats: #Never more than 25 repeats so should be okay...
                indices.pop(rep)
        return indices.popitem(last=False)[1]

if __name__ == "__main__":
    x = Solution()
    print x.firstUniqChar("leetcode")