class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequencies = {}
        for elem in nums:
            if elem not in frequencies:
                frequencies[elem] = 1
            else:
                frequencies[elem] += 1
        for k, v in frequencies.items():
            if v == 1:
                return k
        return -1

l = [1,2,1,3,3]
s = Solution()
print s.singleNumber(l)