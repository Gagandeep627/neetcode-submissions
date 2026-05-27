class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        m = len(nums)
        if (m == 1) or (m == 0):
            return nums

        if (m == 2):
            return nums[::-1]


       
        res = [1 for _ in range(m)]
        Temp = nums
        for ndx in range(0 , m):
            Temp = nums.copy()

            Temp.pop(ndx)

            for i in Temp:
                res[ndx] = res[ndx] * i 

            


        return res


            


        