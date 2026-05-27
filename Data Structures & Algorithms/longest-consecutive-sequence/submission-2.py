class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if not nums:
            return 0

        #time O(n * log(n))
        # space O(n)
        hashed = sorted(set(nums))

        n = len(hashed)
        longest = 1
        curr_streak = 1

        # O(n)
        for i in range(1 , n):
            if hashed[i-1] + 1 == hashed[i]:
                curr_streak += 1
            else:
                longest = max(longest, curr_streak)
                curr_streak = 1

        
        
        # time complexi : O(n * log(n))
        # # space O(n)
        return max(longest , curr_streak)







            

        

        