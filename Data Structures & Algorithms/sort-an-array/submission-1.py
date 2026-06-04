class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        # topic : optimal approach (merge sort Functions) :-

        # stable sorting
        # guaranteed O(n log(n))
        # predictable performance
        # foundation of divide & conquer algorithm
        # easy tric divide - sort - merge |


        # merge sort functions
        def merge_sort(nums):
            
            # base case :
            # if arraya has 0 or 1 elements 
            # its already sorted
            if len(nums) <= 1:
                return nums

            # find middle indes : used divide array into 2 halves
            mid = len(nums) // 2

            # time compledxity : 
            # splitting at log N levels


            # recursively sort left half

            left = merge_sort(nums[:mid])

            # recursively sort right half
            right = merge_sort(nums[mid:])

            # merging at each n level
            # total : O(n log(n))

            # merge the both sorted halfs
            return merge(left, right)

        # merge functions
        # purpose : 
        # combine 2 already sorted arrays
        # into one sorted array

        def merge(left, right):

            # space : O(n)
            #  bcz temporary arrays are created during merging.
            
            # result array : stores final merged sorted elements
            res = []
            l, r = left, right

             # POINTERS
            # i -> pointer for left array
            # j -> pointer for right array
            i = 0
            j = 0


             # COMPARE ELEMENTS OF BOTH ARRAYS
            # Smaller element is added fi

            while i < len(l) and j < len(r):
                 # IF LEFT ELEMENT IS SMALLER
                # Add left element into result
                # and move left pointer.
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1

                # IF RIGHT ELEMENT IS SMALLER
                # Add right element into result
                # and move right pointer.
                else:
                    res.append(r[j])
                    j += 1

            

            # left out elements in l
            # add remaining left elments
            # if left array still has elements
            while (i < len(l)):
                res.append(l[i])
                i += 1

            # add remaining right elements
            # if right array still has elements

            while (j < len(r)):
                res.append(r[j])
                j += 1


            # return final merged sorted array
            return res    

        # start merge sort -->
        answer = merge_sort(nums)
        return answer
