class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = {} 

        # topic : Recursion ++ Memoization Version force solutions -->

        def recurse(i,h):

            if (i >= n):
                return 0

            if (i,h) in dp:
                return dp[(i,h)]

            if (h == 0):
                buy = -prices[i] + recurse(i + 1, 1)
                skip = recurse(i+1,0)

                dp[(i, h)] = max(buy, skip)

            else: #h --> 1

                sell = +prices[i] + recurse(i + 2, 0) #colldown of the stock so skip --> 1 more ((i + 1) +1)-->
                skip = recurse(i+1, 1)

                dp[(i,h)] = max(sell, skip)

            
            return dp[(i,h)]



        index, holding = 0, 0


# | Complexity Type      | Value      |
# | -------------------- | ---------- |
# | **Time Complexity**  | ⭐ **O(n)** |
# | **Space Complexity** | ⭐ **O(n)** |




        return recurse(index, holding)
            


        