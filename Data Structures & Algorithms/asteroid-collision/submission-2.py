class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # In the worst case (no collisions), all asteroids remain in the stack.
        s = [] #stores surviving asteroids




        # process every asteroid
        # O(n)
        # each asteroid is pushed onto the stack at most once and popped at most once.
        for a in asteroids:

            isalive =  True #assume current asteroid survives.


            # collision is only possible only when 
            # stack top is moving right (+)
            # and current asteroid is moving left (-)
            while ((isalive) and (s) and (s[-1] > 0) and (a<0)):


                # stack top (asteroid) is smaller than current asteroid

                # stack top is smaller.
                if (abs(s[-1]) < abs(a)):
                    s.pop() #destroy the stack top
                    

                # stack top (asteroid) is equal than current asteroid

                # both are equal (stack top && asteroid magnitude)
                elif (abs(s[-1]) == abs(a)):
                    s.pop() # destroy stack top
                    isalive = False # current asteroid also explodes

                # stack top (asteroid) is greater // heaviet than current asteroid

                # else suppose stack top is bigger than asteroid's magnitude.
                else:
                    isalive = False #current asteroid explodes.


            # if the current asteroid is still alive.
            # add it to the stack.

            if (isalive == True):
                s.append(a)

        # answer is our stack return it;
        ans = s

        return ans


#         Time Complexity: O(n) — Each asteroid is pushed onto the stack at most once and popped at most once.
# Space Complexity: O(n) — In the worst case (no collisions), all asteroids remain in the stack.

        

            














        




















































































#         changed = True

#         # Keep checking until no collision happens.

#         # O(n)
#         while (changed):

#             changed = False # Assume no collision in this pass.

#             i = 0

#              # Traverse adjacent asteroids.

#             #  O(n)
#             while (i < len(asteroids)-1):

#                 # changed = True
#                  # Collision is possible only when left moves right
#                 # and right moves left.
#                 if ((asteroids[i] > 0) and (asteroids[i+1] < 0)):
                    
#                     # changed = True
#                     # Left asteroid is bigger.
#                     if (abs(asteroids[i]) > abs(asteroids[i+1])):

#                         asteroids.pop(i+1)

#                     # Right asteroid is bigger.

#                     elif (abs(asteroids[i]) < abs(asteroids[i+1])):
#                         asteroids.pop(i)

#                     else: # Both have equal size.
                        
#                         asteroids.pop(i+1)
#                         asteroids.pop(i)
                    
                    
#                     changed = True  # A collision happened.
#                     break # Restart scanning from the beginning.
#                 i += 1



#             # If no collision happened in this pass,
#             # all collisions are finished.
#             if (not changed):
#                 break

# #       Time Complexity: O(n²) in the worst case.
# # Each collision may require restarting the scan, and there can be up to n collisions.
# # Space Complexity: O(1) (ignoring the space used by the input list, since we modify it in place).     
# # time : O(n * n) : O(n ^ 2);

        
#         return asteroids






        