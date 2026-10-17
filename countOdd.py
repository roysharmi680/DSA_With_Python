
class Solution:
    def countOdd(self, arr, n):
        count = 0

        for i in arr:
            if i % 2 != 0:
                count += 1

        return count


# Main program
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

obj = Solution()
print("Number of odd elements =", obj.countOdd(arr, n))
