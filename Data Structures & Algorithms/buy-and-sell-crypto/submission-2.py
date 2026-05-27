class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    
    # 
        # topic : brute force solutions :-
        n = len(prices) #length of prices:
        max_profit = 0 #max_profit set to --> 0
        

        # loop i in range(to (n)):
        for i in range(n):
            # loop j in range(next_to(i), n):
            for j in range(i + 1, n):
                # profit : prices[j] (selled price) - price[i] (buyed price) {for stock}:-
                profit = prices[j] - prices[i]
                if profit > max_profit: # profit goes high than max_profit
                    max_profit = profit # then set max_profit :- profit:- O(n2)

        # time : O(n ^ 2);
        return max_profit #return max_profit calculated:- two nested loops

        #Topic : Sliding_Window
        # sliding window solutions (Optimal Soluitions):-

        # #set left at 0 && right at 1
        # left, right = 0, 1
        # max_profit = 0 #set max_rofit to (0)

        # #untill right is less than (len(prices)):-
        # while (right < len(prices)):
        #     #if right_price > left_price : {sell > buyed price}
        #     if (prices[right] > prices[left]):
        #         # calculate profit via subracting right_price - left_price
        #         profit = (prices[right] - prices[left])
        #         #then evaluate max_profit calcukated so far..
        #         max_profit = max(max_profit , profit)
        #     else:
        #         # if above condition doesnt hold True :-
        #         #then inc (left += 1)
        #         #set right to new_left
        #         #after both loops end inc (rigth += 1)
        #         left += 1
        #         right = left 
            

        #     right += 1

        # #Time_complexity : O(N) for left to be range fro m 0 --> (n - 1) same for right (i --> (n - 1))
        # #Space : O(1)

        # return max_profit #our result is calculated max_profit return it;
        