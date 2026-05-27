class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        

        # topic : greedy : time : O(N-solutions)-->
        start = 0 # to check amount of gas sustaained -- deduced through the container-->
        total = 0 # total gas present from the start to -- n th stations-->
        tank = 0 # total gas present in the tank
        


        for i in range(len(gas)):

            gain = (gas[i] - cost[i])

            total += gain

            tank += gain

            if (tank < 0):

                tank = 0
                start = i+1


        return start if total >= 0 else -1

            
























        # topic : brute force solutions (solutions)..-->

        # n = len(gas)

        # for start in range(n):
        #     tank = 0
        #     valid = True


        #     for step in range(n):
        #         idx = (start + step) % n

        #         tank += gas[idx]
        #         tank -= cost[idx]

        #         if (tank < 0):
        #             valid = False
        #             break

            
        #     if (valid):
        #         return start

        # # valid --> False ->
        # return -1

        
