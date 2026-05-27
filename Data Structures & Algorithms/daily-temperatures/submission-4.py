class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


    # Method : Monoonic_stacks. ++ : ++ ??
        n = len(temperatures)
        res = [0] * (n)
        stack = []


        for i in range(0,n):


            while stack and (temperatures[i] > temperatures[stack[-1]]):
                prev_index = stack.pop()
                res[prev_index] = (i - prev_index)

            stack.append(i)



        return res







        # n = len(temperatures)
        # resultant = [0] * n
        # res_count = 0

        # while (temperatures):
        #     front = temperatures.pop(0)
        #     cnt = 0
        #     for nums in range(0, len(temperatures)):
        #         if (temperatures[nums] > front):
        #             resultant[res_count] = (nums + 1)
        #             res_count += 1
        #             break
        #     # reoccuring vals -->
        #     for xems in temperatures:
        #         if (xems == front):
        #             reccurr_ele_index = temperatures.index(xems)
        #             if (resultant[reccurr_ele_index] == 0):
        #                 resultant[reccurr_ele_index] = resultant[res_count-1]

            
        
        # return resultant









        


        