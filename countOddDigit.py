
class Solution:
    def countOddDigit(self, n):
        count = 0

        while n > 0:
            lastdigit = n % 10

            if lastdigit % 2 != 0:
                count += 1

            n = n // 10

        return count


# Main program
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    sol = Solution()
    result = sol.countOddDigit(n)

    print("Count of odd digits:", result)
