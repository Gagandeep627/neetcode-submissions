class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        # Method Implicit stack_Method Approach -->
        # time_complexity : O(n ^ 2)




        stack = []

        max_area = 0

        heights.append(0) #addition of sentinal bar of height == 0-->



        for i, h in enumerate(heights):


            while (stack) and (heights[stack[-1]] > h):
                max_height = heights[stack.pop()]

                width = i if not stack else (i - stack[-1]) - 1

                max_area = max(max_area, max_height * width)
                

            stack.append(i)



        return max_area
        

                



        