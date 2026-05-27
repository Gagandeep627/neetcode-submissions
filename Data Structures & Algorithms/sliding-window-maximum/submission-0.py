class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        result = []

        for i in range(len(nums) - k + 1):
            window = nums[i : i + k]
            window_max = max(window)
            result.append(window_max)


        return result
        