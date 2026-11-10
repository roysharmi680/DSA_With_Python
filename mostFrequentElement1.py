class Solution:
    # Function to get the highest 
    # occurring element in array nums
    def mostFrequentElement(self, nums):
        
        # Variable to store the size of array
        n = len(nums)
        
        # Variable to store maximum frequency
        maxFreq = 0 
        
        # Variable to store element 
        # with maximum frequency
        maxEle = 0
        
        # Visited array
        visited = [False] * n
        
        # First loop
        for i in range(n):
            # Skip second loop if already visited
            if visited[i]:
                continue
            
            # Variable to store frequency
            # of current element 
            freq = 0
            
            # Second loop
            for j in range(i, n):
                if nums[i] == nums[j]:
                    freq += 1
                    visited[j] = True
            
            # Update variables if new element having 
            # highest frequency is found
            if freq > maxFreq:
                maxFreq = freq
                maxEle = nums[i]
            elif freq == maxFreq:
                maxEle = min(maxEle, nums[i])
        
        # Return the result
        return maxEle

if __name__ == "__main__":
    nums = [4, 4, 5, 5, 6]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to get the
    # highest occurring element in array nums
    ans = sol.mostFrequentElement(nums)
    
    print("The highest occurring element in the array is:", ans)