class Solution:
    def longestConsecutive(self, nums):
        n= len(nums)
        if n == 0:
            return 0 
        longest = 1
        st = set()
        for i in range(n):
            st.add(nums[i])
        for num in st:
            if num-1 not in st:
                count = 1
                x= num
                while x+1 in st:
                    x += 1
                    count += 1 
                longest = max ( longest, count)
        return longest

