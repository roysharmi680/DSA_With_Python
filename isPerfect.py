
class Solution:
    def isPerfect(self, n: int) -> bool:
        if n <= 1:
            return False

        total = 1
        i = 2

        while i * i <= n:
            if n % i == 0:
                total += i

                if i != n // i:
                    total += n // i

            i += 1

        return total == n


# Main program
n = int(input("Enter an integer: "))

obj = Solution()
result = obj.isPerfect(n)

print(result)
