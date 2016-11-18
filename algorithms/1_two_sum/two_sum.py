class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = {}
        for i in xrange(len(nums)):
            comp = target - nums[i]
            if comp in my_map:
                return [my_map[comp], i]
            my_map[nums[i]] = i
        raise Exception("No Solution Found!")
