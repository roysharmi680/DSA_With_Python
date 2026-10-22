
from collections import defaultdict

class Solution:
    def secondMostFrequentElement(self, nums):
        maxfreq = 0
        secmaxfreq = 0
        maxele = -1
        secele = -1

        mapp = defaultdict(int)

        for i in nums:
            mapp[i] += 1

        for ele, freq in mapp.items():
            if freq > maxfreq:
                secmaxfreq = maxfreq
                maxfreq = freq
                secele = maxele
                maxele = ele

            elif freq == maxfreq:
                maxele = min(maxele, ele)

            elif freq > secmaxfreq:
                secmaxfreq = freq
                secele = ele

            elif freq == secmaxfreq:
                secele = min(secele, ele)

        return secele


# Main program
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

obj = Solution()
result = obj.secondMostFrequentElement(nums)

print("Second most frequent element:", result)
