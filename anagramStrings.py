class Solution:
    def anagramStrings(self, s, t):
        # If lengths are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    solution = Solution()
    str1 = "INTEGER"
    str2 = "TEGERNI"
    result = solution.anagramStrings(str1, str2)
    print("True" if result else "False")