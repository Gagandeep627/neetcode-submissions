class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    



    # try yourself first for logic if not worked then go for the solution 
    # provided by different competent sources // --> just start doing ur wrk shift
    # bass start doing ur wrk shift , hune te better he kii Move to nxt wrk. ++ : ++ ??

    

        # optimal approach --> dictionary -- hashmap approach -->



        anagram_map = {}




        for word in strs:

            sorted_word = "".join((sorted(word)))


            if sorted_word not in anagram_map.keys():
                anagram_map[sorted_word] = []
            
            anagram_map[sorted_word].append(word)


        return list(anagram_map.values())

            

            








            

