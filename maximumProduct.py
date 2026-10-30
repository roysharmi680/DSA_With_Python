
class Solution:
    def maximumProduct(self, nums):
        nums.sort()

        n = len(nums)

        # Case 1: Product of three largest numbers
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        # Case 2: Product of two smallest and one largest
        product2 = nums[0] * nums[1] * nums[n - 1]

        return max(product1, product2)


# Main program
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

obj = Solution()
result = obj.maximumProduct(nums)

print("Maximum product:", result)
