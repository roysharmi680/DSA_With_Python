
class Solution:
    def mostFrequentElement(self, nums):
        maxfreq = 0
        maxitem = 0
        temp = {}

        for i in nums:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1

        for ele, freq in temp.items():
            if freq > maxfreq:
                maxfreq = freq
                maxitem = ele
            elif freq == maxfreq:
                maxitem = min(maxitem, ele)

        return maxitem


# Main program
nums = list(map(int, input("Enter array elements: ").split()))

obj = Solution()
print("Most frequent element =", obj.mostFrequentElement(nums))
