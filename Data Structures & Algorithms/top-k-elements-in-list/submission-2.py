class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        # ajj day , date : saturday , 11 th oct. ++ : ++ ??

            freq_map = {}

            # calculated freq for each element stored num : freq in the mapped_dictionary...
            for num in nums:
                freq_map[num] = freq_map.get(num , 0) + 1

            

            # created a bucket for length --> nums...

            bucket = [[] for _ in range(len(nums) + 1)] 
            

            # for each index --> (frequency) --> added (num) to the busket[index : freq]


            for num , freq in freq_map.items():
                # for num in nums:
                bucket[freq].append(num)

           



            

            # for index -- > last index to the bucket --> checked for nums in that particular//
            # at particular index -- called as (freq) --> added (nums) --> result && after k the most occuring elements are found then//
            # we have returned the list(result) -->//
            result = []
            for index in range(len(nums), 0 , -1):
                for nums in bucket[index]:
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

         









