class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        # topic : optimal approach (merge sort algorithm) :-


        def merge_sort(nums):

            if len(nums) <= 1:
                return nums


            mid = len(nums) // 2

            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])


            return merge(left, right)


        def merge(left, right):


            res = []
            l, r = left, right
            i = 0
            j = 0


            while i < len(l) and j < len(r):
                
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1

                else:
                    res.append(r[j])
                    j += 1

            

            # left out elements in l

            while (i < len(l)):
                res.append(l[i])
                i += 1

            while (j < len(r)):
                res.append(r[j])
                j += 1



            return res    


        answer = merge_sort(nums)
        return answer
