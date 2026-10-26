class Solution:
    # Function to check if a given string is a palindrome
    def palindromeCheck(self, s):
        left = 0               
        right = len(s) - 1     

        # Iterate while  start pointer is less than end pointer
        while left < right:
            # If characters  don't match, it's not a palindrome
            if s[left] != s[right]:
                return False
            left += 1  
            right -= 1  
        return True 

if __name__ == "__main__":
    solution = Solution()
    str = "racecar"  

    if solution.palindromeCheck(str):
        print(f"{str} is a palindrome.")
    else:
        print(f"{str} is not a palindrome.")