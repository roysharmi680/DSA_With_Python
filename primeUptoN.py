
import math

class Solution:
    def primeUptoN(self, n):
        count = 0

        for i in range(n + 1):
            if self.isPrime(i):
                count += 1

        return count

    def isPrime(self, n):
        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True


# Main program
n = int(input("Enter a number: "))

obj = Solution()
print("Number of primes up to", n, "=", obj.primeUptoN(n))
