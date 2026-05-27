class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    



    # try yourself first for logic if not worked then go for the solution 
    # provided by different competent sources // --> just start doing ur wrk shift
    # bass start doing ur wrk shift , hune te better he kii Move to nxt wrk. ++ : ++ ??

        # Brute-force Solution -->


        def are_anagrams(s ,t):

            if (len(s) != len(t)):
                return False

            return (sorted(s) == sorted(t))

            

        m = len(strs)

        resultant = []
        visited = [False] * m


        for i in range(0, m):

            if (visited[i] == True):
                continue

            group = [strs[i]]
            visited[i] = True


            for j in range(i + 1 , m):
                if not visited[j] and are_anagrams(strs[i], strs[j]):
                    visited[j] = True
                    group.append(strs[j])

            
            resultant.append(group)
             
           


        return resultant

        
            






























        # optimal approach --> dictionary -- hashmap approach -->



        # anagram_map = {}




        # for word in strs:

        #     sorted_word = "".join((sorted(word)))


        #     if sorted_word not in anagram_map.keys():
        #         anagram_map[sorted_word] = []
            
        #     anagram_map[sorted_word].append(word)


        # return list(anagram_map.values())

            

            








            

