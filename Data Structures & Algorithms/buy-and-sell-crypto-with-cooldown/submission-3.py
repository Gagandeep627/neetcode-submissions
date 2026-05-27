class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = {} #memo cache-->

        # topic : Recursion ++ Memoization Version force solutions -->

        def recurse(i,h):
            

            # base case : no more days-->
            if (i >= n):
                return 0


            # if we have solved this state
            # before, return cached value-->
            if (i,h) in dp:
                return dp[(i,h)]

            # if we are not holding a stock now --> 
            # we can buy or skip-->
            if (h == 0):
                buy = -prices[i] + recurse(i + 1, 1) #buy today
                skip = recurse(i+1,0) #skip today

                dp[(i, h)] = max(buy, skip)


            # if we are holding a stock -> we can sell or skip
            else: #h --> 1
                # sell today + cooldown
                sell = +prices[i] + recurse(i + 2, 0) #colldown of the stock so skip --> 1 more ((i + 1) +1)-->
                # skip today
                skip = recurse(i+1, 1)

                dp[(i,h)] = max(sell, skip)

            
            return dp[(i,h)]



        index, holding = 0, 0


# | Complexity Type      | Value      |
# | -------------------- | ---------- |
# | **Time Complexity**  | ⭐ **O(n)** |
# | **Space Complexity** | ⭐ **O(n)** |




        return recurse(index, holding)
            


        