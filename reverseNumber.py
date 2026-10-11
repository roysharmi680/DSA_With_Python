
class Solution:
    def reverseNumber(self, n):
        temp = 0
        revnum = 0

        while n > 0:
            temp = n % 10
            revnum = revnum * 10 + temp
            n = n // 10

        return revnum


# Main program
n = int(input("Enter a number: "))

obj = Solution()
result = obj.reverseNumber(n)

print("Reversed number:", result)
