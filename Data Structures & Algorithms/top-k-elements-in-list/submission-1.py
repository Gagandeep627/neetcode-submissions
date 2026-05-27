class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        # ajj day , date : saturday , 11 th oct. ++ : ++ ??

            freq_map = {}


            


            for num in nums:
                freq_map[num] = freq_map.get(num , 0) + 1


            bucket = [[] for _ in range(len(nums) + 1)]

            for num , freq in freq_map.items():
                bucket[freq].append(num)


            result = []
            for i in range(len(nums), 0 , -1):
                for nums in bucket[i]:
                    result.append(nums)
                    if (len(result) == k):
                        return result















        # unique elements -->
        # hashed = set(i for i in nums)

        # containing_top_all = {}



        # # count for each unique element stored in the dict(containing_top_all)
        # for j in hashed:
        #     containing_top_all[j] = nums.count(j)
        
        # d = containing_top_all
        # # sorting of the dictionary as per values for each key
        # # item in the dictionary..
        # sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        # res, i = [], 0
        # while k != 0 and hashed:
            
        #     first = next(iter(sorted_dict))#first key value of dict
        #     res.append(first) #added to result..
        #     sorted_dict.pop(first) #removed that first element from dictionary...
        #     k -= 1


        # return res

         









