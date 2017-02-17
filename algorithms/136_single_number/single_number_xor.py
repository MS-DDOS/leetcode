class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for elem in nums:
            result ^= elem
        return result

l = [1,2,1,3,3]
s = Solution()
print s.singleNumber(l)