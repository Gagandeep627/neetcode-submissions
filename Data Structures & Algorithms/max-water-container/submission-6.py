class Solution:
    def maxArea(self, heights: List[int]) -> int:



        # Method 1: optimal approach via 2 pointer approach : O(n ^ 2) approach of solns:

        start = 0
        end = len(heights) - 1


        max_area = 0


        while (start < end):

            width = (end - start)
            area = min(heights[start], heights[end]) * (width)

            max_area = max(max_area, area)


            if (heights[start] < heights[end]):
                start += 1
            else:
                end -= 1

        return max_area





            



