import math
class Solution:
    def minimumRateToEatBananas(self, nums, h):
      low= 1
      high = self.findmax(nums)
      while low <= high:
        mid= low + ( high -low) //2 
        totalh = self.totalhours(nums, mid)
        if totalh <= h:
          high = mid-1
        else:
          low = mid +1
      return low
      

    def totalhours(self, nums , hour):
      totalh = 0
      n= len(nums)
      for i in range(n):
        totalh += math.ceil(nums[i]/hour)
      return totalh
    def findmax(self, nums):
      maxi = float('-inf')
      n= len(nums)
      for i in range(n):
        maxi = max (maxi, nums[i])
      return maxi
       