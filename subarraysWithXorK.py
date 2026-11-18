
class Solution:
    def subarraysWithXorK(self, nums, k):
        xr = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            xr ^= num

            x = xr ^ k

            count += freq.get(x, 0)

            freq[xr] = freq.get(xr, 0) + 1

        return count
