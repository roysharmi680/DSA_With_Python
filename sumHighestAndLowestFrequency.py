
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        n = len(nums)
        maxfreq = 0
        minfreq = n
        mapp = {}

        # Count the frequency of each element
        for i in nums:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1

        # Find the highest and lowest frequencies
        for freq in mapp.values():
            maxfreq = max(maxfreq, freq)
            minfreq = min(minfreq, freq)

        return maxfreq + minfreq


# Main program
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

obj = Solution()
result = obj.sumHighestAndLowestFrequency(nums)

print("Sum of highest and lowest frequencies:", result)
1