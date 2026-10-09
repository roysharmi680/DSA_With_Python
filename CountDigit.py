
class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1

        count = 0
        while n > 0:
            n = n // 10
            count += 1

        return count


# Main program
n = int(input("Enter a number: "))

obj = Solution()
result = obj.countDigit(n)

print("Number of digits:", result)
# end code
