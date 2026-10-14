
class Solution:
    def largestDigit(self, n):
        temp = 0
        ldigit = 0

        while n > 0:
            temp = n % 10

            if temp > ldigit:
                ldigit = temp

            n = n // 10

        return ldigit


# Main program
n = int(input("Enter a number: "))

obj = Solution()
result = obj.largestDigit(n)

print("Largest digit =", result)
