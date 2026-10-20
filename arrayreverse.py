
class Solution:
    def reverse(self, arr, n):
        left = 0
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


# Main program
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

obj = Solution()
print("Reversed array =", obj.reverse(arr, n))
