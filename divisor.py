
class Solution:
    def divisors(self, n):
        div = []

        for i in range(1, n + 1):
            if n % i == 0:
                div.append(i)

        return div


# Main program
n = int(input("Enter a number: "))

obj = Solution()
print("Divisors =", obj.divisors(n))
