class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        
                


        # Method: Stack_based_Approach (optimal_approach_for Stack based methodology).. -->
        # Method to follow after this : Stack -->
        # Sorting cars → O(n log n)
        cars_positions = sorted(zip(position , speed), reverse = True)
        stack = []
        


        # Single traversal (stack) → O(n)
        # for al positions , speed --> cars_positions
        for pos, spd in cars_positions:

            time = (target - pos) / spd
            # check if time is less than  or equal to last to the most closedt position to 
            # to the target --> then dont incluse it into the stack else : append it to 
            # the stack..
            if not stack or time > stack[-1]:
                stack.append(time)


        # time complexity : O(n log n) + O(n) : O(n log n). ++ : ++ ??
        # length of stack will give total no. of fleets -->
        return len(stack)

























































        

