class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.



        #  aim for a solution with O(n) time and O(n) space,
        #  where n is the size of the input array.




        # using hash map / dictionary method for teh method of hash map and dictionary
        # to..

# SC : O(n)
        num_to_index = {}
        n = len(nums)
# TC : O(n)
        for i in range(0, n):
            # calculates value to be find out..
            complement = target - nums[i]
            # checking whether  complement is present in the num_to_index
            if (complement not in num_to_index):
                num_to_index[nums[i]] = i
            else:
                # if got complement then return [index where the previous find to element is fount whose sum with the nums[i] == target , i(index where the next elemnt is found computes sum to getting to the target...)]
                return [num_to_index[complement], i]




























# Tc : O(n)
# S.C : o(n)
# brute force approach of solving the problem -->
# space O(1)
        n = len(nums)

# time complex : Complexity:

# Time: O(n²) — two nested loops
# space complexity : Space: O(1) — no extra space
        if ((len(nums) == 2) and (sum(nums) == target)):
            return [0,1]

# Time : (n(1) * n(2) = n ^ 2)
# space O(1)
        for i in range(0, n):
            for j in range(i + 1 , n):
                
                if ((nums[i] + nums[j]) == target):
                    return [i, j]




        