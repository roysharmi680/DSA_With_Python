
class Solution:
    def removeDuplicates(self, arr):
        result = []
        seen = set()

        for num in arr:
            if num not in seen:
                result.append(num)
                seen.add(num)

        return result


def main():
    arr = list(map(int, input("Enter array elements: ").split()))

    obj = Solution()
    result = obj.removeDuplicates(arr)

    print("Array after removing duplicates:", result)


if __name__ == "__main__":
    main()
