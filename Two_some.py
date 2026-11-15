
from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        ans = [-1, -1]

        # Store elements with their original indices
        eleIndex = []

        for i in range(n):
            eleIndex.append([nums[i], i])

        # Sort according to element values
        eleIndex.sort(key=lambda x: x[0])

        # Initialize two pointers
        left, right = 0, n - 1

        while left < right:

            sum_val = eleIndex[left][0] + eleIndex[right][0]

            if sum_val == target:
                ans[0] = eleIndex[left][1]
                ans[1] = eleIndex[right][1]
                return ans

            elif sum_val < target:
                left += 1

            else:
                right -= 1

        return ans


def main():
    nums = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    sol = Solution()
    ans = sol.twoSum(nums, target)

    print("Indices:", ans)


if __name__ == "__main__":
    main()
