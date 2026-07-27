class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:




            # topic : brute force solutions:-
             # List to store (distance from x, actual value)
            
#             Space Complexity: O(n)

# temp stores all n (distance, value) pairs.
            temp = []


            # Traverse every element in the array
            # Traverse array → O(n)
            for num in arr:

                  # Calculate the absolute distance of current number from x
                res = abs(x - num)
                 # Store (distance, value) as a tuple
                temp.append((res, num))


            # sort tuples:
            # 1. smaller distance comes first
            # 2. if distance are equal, smaller value comes first
            # Sort all (distance, value) pairs → O(n log n)
            temp.sort()
            
            # list to store the k closesr elements
            ans = []

            # Pick first k elements → O(k)
            # pick only the first k tuples (the closest elemenrs)
            for i in range(k):
                # extract only the value (index : 1) from each tuple
                ans.append(temp[i][1])


            # sort the selected elements because
            # the problem requires the final answer in ascending order
            
            # Sort answer → O(k log k)
            ans.sort()

            # Overall: O(n log n)
            # return the final sorted list of k closest elements
            return ans
            
