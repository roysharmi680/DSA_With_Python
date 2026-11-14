
class Solution:
    def anagramMappings(self, nums1, nums2):
        index_map = {}

        # Store all indices of elements in nums2
        for i, num in enumerate(nums2):
            if num not in index_map:
                index_map[num] = []

            index_map[num].append(i)

        result = []

        # Find the corresponding index for each element
        for num in nums1:
            result.append(index_map[num].pop())

        return result


def main():
    nums1 = list(map(int, input("Enter nums1: ").split()))
    nums2 = list(map(int, input("Enter nums2: ").split()))

    obj = Solution()
    result = obj.anagramMappings(nums1, nums2)

    print("Index mapping:", result)


if __name__ == "__main__":
    main()
