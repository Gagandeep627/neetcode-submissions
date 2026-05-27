class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)


        # topic : Recursion ++ Brute force solutions -->

        def recurse(i,h):

            if (i >= n):
                return 0

            if (h == 0):
                buy = -prices[i] + recurse(i + 1, 1)
                skip = recurse(i+1,0)

                return max(buy, skip)

            else: #h --> 1

                sell = +prices[i] + recurse(i + 2, 0) #colldown of the stock so skip --> 1 more ((i + 1) +1)-->
                skip = recurse(i+1, 1)

                return max(sell, skip)



        index, holding = 0, 0


        return recurse(index, holding)
            


        