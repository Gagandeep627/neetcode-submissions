class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        # ajj day , date : saturday , 11 th oct. ++ : ++ ??



        hashed = set(i for i in nums)

        containing_top_all = {}




        for j in hashed:
            containing_top_all[j] = nums.count(j)
        
        d = containing_top_all
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        res, i = [], 0
        while k != 0 and hashed:
            
            first = next(iter(sorted_dict))
            res.append(first)
            sorted_dict.pop(first)
            k -= 1


        return res

         









