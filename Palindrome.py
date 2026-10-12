
class Solution:
    def isPalindrome(self, n):
        checkpalindrome = n
        temp = 0
        rev = 0

        while n > 0:
            temp = n % 10
            rev = rev * 10 + temp
            n = n // 10

        if rev == checkpalindrome:
            return True
        else:
            return False


# Main program
n = int(input("Enter a number: "))

obj = Solution()
result = obj.isPalindrome(n)

print(result)
