class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        

        # topic : greedy : time : O(N-solutions)-->

        
        start = 0 # to check amount of gas sustaained -- deduced through the container(candidate starting stations)-->
        total = 0 # total gas present from the start to -- n th stations--> (total gas across the whole journey)
        tank = 0 # total gas present in the tank (gas in tank while scanning->)
        

        # We loop once.
        for i in range(len(gas)):

            gain = (gas[i] - cost[i]) #We use only constant variables.

            total += gain #We use only constant variables.

            tank += gain #We use only constant variables.

            if (tank < 0):

                tank = 0 # reset tank
                start = i+1 # next stations becomes new candidate->


        return start if total >= 0 else -1

        # Time: O(n) 
        # Space: O(1)

            
























        # topic : brute force solutions (solutions)..-->

        # n = len(gas)
        # Because for each of the n stations
        # for start in range(n):
        # Only using a few variables (tank, i, etc.)
        #     tank = 0
        #     valid = True


        #     for step in range(n): , we simulate up to n steps.
        #         idx = (start + step) % n circular move->
        # Only using a few variables (tank, i, etc.)
        #         tank += gas[idx]
        #         tank -= cost[idx]

        #         if (tank < 0):
        #             valid = False
        #             break

            
        #     if (valid):
        #         return start

        # # valid --> False ->
        # return -1

        # Time: O(n²)
        # Space: O(1)

        
