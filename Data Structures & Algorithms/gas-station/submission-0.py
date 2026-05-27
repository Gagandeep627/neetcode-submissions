class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        


        # topic : brute force solutions (solutions)..-->

        n = len(gas)

        for start in range(n):
            tank = 0
            valid = True


            for step in range(n):
                idx = (start + step) % n

                tank += gas[idx]
                tank -= cost[idx]

                if (tank < 0):
                    valid = False
                    break

            
            if (valid):
                return start

        # valid --> False ->
        return -1

        
