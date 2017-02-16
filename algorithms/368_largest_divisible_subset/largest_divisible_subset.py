x = [1,2,3]
y = [1,2,4,8]
z = [1,2,4,5,6,12]

import numpy as np

class Solution(object):

    def largestDivSubset(self, nums):
        res = []
        if not nums:
            return res
        nums = np.array(nums)
        nums.sort()
        dp = np.zeros(len(nums))
        #dp = [0 for _ in range(len(nums))]
        dp[0] = 1

        for i in xrange(1, len(nums)):
            for j in range(i)[::-1]:
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_index = 0
        for i in xrange(1,len(nums)):
            if dp[i] > dp[max_index]:
                max_index = i

        temp = nums[max_index]
        curDp = dp[max_index]
        for i in range(max_index,-1,-1):
            print i
            if temp % nums[i] == 0 and dp[i] == curDp:
                res.append(nums[i])
                temp = nums[i]
                curDp -= 1

        return res

    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
            print S
        return list(max(S.values(), key=len))

    def lds(self, nums):
        buckets = {-1:set()}
        for x in sorted(nums):
            candidates = []
            for s in buckets:
                if x % s == 0:
                    candidates.append(buckets[s])
            print buckets
            buckets[x] = max(candidates, key=len).union(set([x])) # take all other things the number is divisible by and add itself.
        return list(max(buckets.values(), key=len)) # choose the LARGEST divisible subset


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

import timeit
s = Solution()

'''
withSet = wrapper(s.largestDivisibleSubset, x)
withList = wrapper(s.largestDivisibleSubset2, x)
print timeit.timeit(withSet, number = 1000)
print timeit.timeit(withList, number = 1000)

withSet = wrapper(s.largestDivisibleSubset, y)
withList = wrapper(s.largestDivisibleSubset2, y)
print timeit.timeit(withSet, number = 1000)
print timeit.timeit(withList, number = 1000)
'''

#print s.largestDivisibleSubset2(x)
#print s.largestDivisibleSubset2(y)
#print "--------"
print s.largestDivSubset(x)
print
print s.largestDivSubset(y)
print "--------"
print s.largestDivSubset(z)
print "________"
print s.largestDivisibleSubset(z)
print "--------"
print s.lds(z)