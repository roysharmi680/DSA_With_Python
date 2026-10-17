
class Solution:
    def sum(self, arr, n):
        total = 0

        for i in range(n):
            total = total + arr[i]

        return total


# Main program
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

obj = Solution()
print("Sum =", obj.sum(arr, n))
