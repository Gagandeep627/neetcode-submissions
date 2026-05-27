class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if not nums:
            return 0


        hashed = sorted(set(nums))

        n = len(hashed)
        longest = 1
        curr_streak = 1


        for i in range(1 , n):
            if hashed[i-1] + 1 == hashed[i]:
                curr_streak += 1
            else:
                longest = max(longest, curr_streak)
                curr_streak = 1

        
        return max(longest , curr_streak)







            

        

        