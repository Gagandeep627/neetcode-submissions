class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


        # topic brute force solutions:-

        
        #set res = 0
        res = 0

        # loop i in range(0, len(heights)):-
        # O(n)
        for i in range(len(heights)):
            # loop j in  range(i + 1, len(heights)):-
            # O(n)
            for j in range(i + 1, len(heights)):
                # take min(heights[i], heights[j]) #height of the container possible
                # width of the container : (end-start) : (j-i)
                # multiplication of both of above will lead to container with the most water ~ (3)
                # maintain the container with most of water
                # via max function (res, calculated (3) water conatainer for the bucket so far)
                # maintain the maximum container filled with water so far required..
                # store above in res;

                #answer : res
                res = max(res, min(heights[i], heights[j]) * (j - i))
        
        # return answer;
        # time_complexity :O(n * n) : O(n ^ 2);
        return res


















































































