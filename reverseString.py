
class Solution:
    def reverseString(self, s):
        temp = []

        for i in s:
            temp.append(i)

        for j in range(len(s)):
            s[j] = temp.pop()

        return s


# Main program
s = list(input("Enter a string: "))

obj = Solution()
result = obj.reverseString(s)

print("Reversed string:", "".join(result))
