class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


    # Method : Monoonic_stacks. ++ : ++ ??
#         n = len(temperatures)
#         # storing temperauture distant..
#         res = [0] * (n)
#         # storing for elements indexed..
#         stack = []
#         for i in range(0,n):
#             # checking whether i th index element is greater
#             # than previous element..
#             # if yes -- take prev_index and store how much it is far away from
#             # that temperature...
#             while stack and (temperatures[i] > temperatures[stack[-1]]):
#                 prev_index = stack.pop()
#                 res[prev_index] = (i - prev_index)
#             # always store i th index to the stack in order to comparison for the next
#             # i th indexed element..
#             stack.append(i)
#  # return resulatnt -->
#         return res

        n = len(temperatures)
        result = [0] * n  # Initialize result list

        # Outer loop → pick each day
        for i in range(n):
            # Inner loop → look ahead for warmer day
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i  # number of days until warmer
                    break  # stop at the first warmer day
        
        return result  








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









        


        