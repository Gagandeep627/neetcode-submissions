class Solution:
    def trap(self, height: List[int]) -> int:


        # method 1 : Brute-force-concept explained easily..


        n = len(height)
        water = 0

        if not height:
            return 0

        for i in range(n):


            max_left = max(height[:i + 1])


            max_right = max(height[i:])



            trapped = min(max_left, max_right) - height[i]


            if (trapped > 0):
                water += trapped



        
        return water




        




































        # topic : 2 pointer approach -->

        
































#         left = 0
#         right = len(height) - 1


#         left_max = 0
#         right_max = 0
#         water = 0


#         while (left < right):
#             # case 1 : left side is smaller...
#             if (height[left] < height[right]):
#                 if (height[left] >= left_max):
#                     left_max = height[left]
#                 else:
#                     water += (left_max - height[left])

#                 left += 1

#             else:
#             # case 2 : right side is smaller or equal to the left side...
#                 if (height[right] >= right_max):
#                     right_max = height[right]
#                 else:
#                     water += (right_max - height[right])

#                 right -= 1



#         # ⏱️ Time and Space Complexity

# # Time: O(n) → each element visited once

# # Space: O(1) → constant extra memory
# # ✅ Most optimal solution for “Trapping Rain Water.”
        

#         return abs(water)

                




                 

           


                
                    


                

            


       
        

