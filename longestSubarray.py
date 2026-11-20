class Solution:
    def longestSubarray(self, nums, k):

        n= len(nums)
        presummap= {}
        sum = 0
        maxlen = 0
        for i in range(n):
            sum += nums[i]
            if sum == k:
                maxlen= max(maxlen, i+1)
            rem = sum - k
            if rem in presummap:
                length = i - presummap[rem]
                maxlen = max( maxlen, length)
            if sum not in presummap:
                presummap[sum] = i 
        return maxlen
        