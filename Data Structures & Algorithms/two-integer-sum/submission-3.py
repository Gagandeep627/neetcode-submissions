class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

# Tc : O(n)
# S.C : o(n)
# brute force approach of solving the problem -->
        n = len(nums)


        if ((len(nums) == 2) and (sum(nums) == target)):
            return [0,1]


        for i in range(0, n):
            for j in range(i + 1 , n):
                
                if ((nums[i] + nums[j]) == target):
                    return [i, j]




        