class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        n = len(nums)
        min_len = float("inf")



        for i in range(0, n):
            

            curr = 0

            for j in range(i, n):

                curr += nums[j]


                if (curr >= target):
                    
                    length = (j - i + 1)

                    min_len = min(min_len, length)

                    break

        if (min_len == float("inf")):
            return 0

        return min_len
