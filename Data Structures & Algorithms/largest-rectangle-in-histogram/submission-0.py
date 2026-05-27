class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:




        res = max(heights)
        n = len(heights)


        for i in range(n):
            for j in range(i + 1, n):

                min_height = min(heights[i:j+1])

                breadth = (j+1 - i)


                area_calculated = (min_height * breadth)


                if res <= area_calculated:
                    res = area_calculated


        return res

                



        