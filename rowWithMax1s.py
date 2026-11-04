class Solution:
    def rowWithMax1s(self, mat):
        max_count = 0
        ans = -1

        for i in range(len(mat)):
            count = mat[i].count(1)

            if count > max_count:
                max_count = count
                ans = i

        return ans


# Main function
if __name__ == "__main__":
    mat = [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 0]
    ]

    obj = Solution()
    result = obj.rowWithMax1s(mat)

    print("Row with maximum 1s:", result)