
class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                return False

        return True


# Main program
arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

obj = Solution()
result = obj.arraySortedOrNot(arr, n)

if result:
    print("Array is sorted")
else:
    print("Array is not sorted")