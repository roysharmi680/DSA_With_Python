class Solution:
    def NnumbersSum(self, N):
        # Base case: if N is 0, return 0
        if N == 0:
            return 0
        # Recursive case: add N to the sum of N-1
        return N + self.NnumbersSum(N - 1)

if __name__ == "__main__":
    solution = Solution()
    N = 10 # Example input
    print(f"Sum of first {N} numbers is {solution.NnumbersSum(N)}")