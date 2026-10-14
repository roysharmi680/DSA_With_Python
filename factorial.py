
class Solution:
    def factorial(self, n):
        if n == 0:
            return 1

        fact = 1
        for i in range(1, n + 1):
            fact = fact * i

        return fact


# Main program
n = int(input("Enter a number: "))

obj = Solution()
print("Factorial =", obj.factorial(n))
