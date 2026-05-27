class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        


        # Method: Stack_based_Approach -->
        # Method to follow after this : Stack -->

        cars_positions = sorted(zip(position , speed), reverse = True)
        stack = []
        



        for pos, spd in cars_positions:

            # pos, spd = cars_positions.pop(0)


            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)


            
        return len(stack)

























































        

