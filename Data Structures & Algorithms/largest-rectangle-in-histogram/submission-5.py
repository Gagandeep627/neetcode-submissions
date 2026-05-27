class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        # Method Implicit stack_Method Approach -->
        # time_complexity : O(n)




        stack = []

        max_area = 0
        #for all the left out values at the end then --> will be compared with 0
        # then which will be higher than the height 0 so all the rectangles corrrosponding to 
        # the left out heights will beb meaqsured and the max_area will be reevaluated 
        # to its max area possible so far...
        heights.append(0) #addition of sentinal bar of height == 0-->


        # time : O(n)
        for i, h in enumerate(heights):

            # if previous height is > than next height
            # tme : O(0 -- i : not (i + 1 -- N))
            while (stack) and (heights[stack[-1]] > h):
                max_height = heights[stack.pop()] #store height and remove its index from  stack..

                width = i if not stack else (i - stack[-1]) - 1 #width : i if not stack else (current_index - previous_index - 1)

                max_area = max(max_area, max_height * width) #calculate max_area of rrectangle
                

            stack.append(i)


        # time : O(n) --> loop for heights..
        # space : O(n) --> stack..
        return max_area
        

                



        