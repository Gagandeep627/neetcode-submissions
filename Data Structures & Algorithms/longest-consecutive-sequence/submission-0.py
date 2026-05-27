class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:




        if not nums:
            return 0

        hashed = sorted(set(nums))   # remove duplicates and sort
        longest = 1
        current_streak = 1

        for i in range(1, len(hashed)):
            if hashed[i] == hashed[i - 1] + 1:
                current_streak += 1
            else:
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)
            

        

        # return len(hashed)