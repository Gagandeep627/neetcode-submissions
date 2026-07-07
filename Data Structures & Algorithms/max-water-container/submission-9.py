class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


        # # Method 1: optimal approach via 2 pointer approach : O(n ^ 2) approach of solns:


        # # set start : 0
        # start = 0

        # # set end : len(heights) - 1
        # end = len(heights) - 1

        # # set max_area : 0
        # max_area = 0

        # # loop untill (start reaches the end):-

        # # max to max start will reaches the end ;
        # # O(N);
        # while (start < end):
            
        #     # validate its width :
        #     # (end - start)
        #     width = (end - start)

        #     # check area : take minimum (heights[start], heights[end]) * (width);
        #     area = min(heights[start], heights[end]) * (width)

        #     # evaluate the maximum_area : 
        #     # max of (max_area, area);
        #     max_area = max(max_area, area)

            
            
        #     # now lets check heights(corrosponding start wil be less than end):-
        #     # now validate if height(start) is lesser than height(end)
        #     # it means : heights[start+1] may be higher than height[start]
        #     # as the area will be dependable to mins(heights[start], heighs[end])
        #     # so lets have a hypothetical supposition that
        #     # heights corrosponding (start + 1) may have the higher value
        #     # heights(start);
        #     if (heights[start] < heights[end]):
        #         # increment start += 1
        #         start += 1
        #     else:

        #         # and in similar way suppose heights(end) is lower than heights(start)
        #         # means : now lets suppose heights(end - 1) will be higgher than  heights(end)
        #         # heights(end-1) may be higher than heights(end) then : as minimum of
        #         # minimum of heights(start, end) may corrosponding to the higher value 
        #         # as better than the previous heights
        #         end -= 1


        # # return ans : max_area;
        # return max_area


        #topic : optimal solutions (for the above approach)->
        
        # Method 1: optimal approach via 2 pointer approach : O(n ^ 2) approach of solns:

        # start = 0 # set start  : 0
        # end = len(heights) - 1 # set end : len(heights)-1


        # max_area = 0 # set max_area : 0

        # # loop untill start < end:
        # # each height(index) is visited once
        # # time : O(n)
        # while (start < end):
        #     # evaluate width : to be (end-start)
        #     width = (end - start)
        #     # evaluate minimum of heights[start], heights[end] 
        #     # multiplied by (width)
        #     # this will evaluate to area
        #     area = min(heights[start], heights[end]) * (width)
            

        #     # but we have to evaluate the maximum area
        #     # store the updated maximum area in the max_area
        #     # variable->
        #     max_area = max(max_area, area)

        #     # if height corrosponding to start will be lesser than height corrosponding to 
        #     # the end:
        #     if (heights[start] < heights[end]):
        #         # ~(1)
        #         # a imaginary on consideration case that the start += 1
        #         # may have the height[i] > height[start]
        #         # move to a container (which may contain mopre water capacity):
        #         # so move start to 1 
        #         start += 1
        #     else:#otherwise
        #         # suppose : height[start] is more than height[end]
        #         # then lets suppose the height[end-1] may assume to be height which
        #         # will be more height than height[end] 
        #         # so move end -= 1
        #         # same supposition as ~(1)
        #         end -= 1


        # # answer : max_area
        # # return answer;
        # return max_area


        # topic : brute force solutions:-
        # topic brute force solutions:-
        # topic : brute force solutions:

        #set res : 0
        res = 0

        # loop i in range(0, len(heights)):-
        # loop i in range(0, len(heights)):-
        # O(n)
        # O(n)
        for i in range(len(heights)):
            # loop j in  range(i + 1, len(heights)):-
            # O(n)

            # loop j in range(i+1, len(heights)):-
            # O(n) --> O(n ^ n) --> time_complexity --> O(n ^ 2);
            for j in range(i + 1, len(heights)):
                # take min(heights[i], heights[j]) #height of the container possible
                # width of the container : (end-start) : (j-i)
                # multiplication of both of above will lead to container with the most water ~ (3)
                # maintain the container with most of water
                # via max function (res, calculated (3) water conatainer for the bucket so far)
                # maintain the maximum container filled with water so far required..
                # store above in res;

                #answer : res
                heightuptil_water_may_arise = min(heights[i], heights[j])
                # resultant : maximum(resultant, minimum(heights[i], heights[j]) * (j-1))
               
                water_contained_uptill_height = heightuptil_water_may_arise * (j - i)
               
                res = max(res, water_contained_uptill_height)
                
        
        # return answer; set res : answer;
        # time_complexity :O(n * n) : O(n ^ 2);
        # return answer;
        return res


















































































