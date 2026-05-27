class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    



    # try yourself first for logic if not worked then go for the solution 
    # provided by different competent sources // --> just start doing ur wrk shift
    # bass start doing ur wrk shift , hune te better he kii Move to nxt wrk. ++ : ++ ??

    

        def to_check_Anagram(s, t):
            if len(s) != len(t):
                return False
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] += 1
                arr[ord(t[i]) - ord('a')] -= 1
            for j in arr:
                if j != 0:
                    return False
            return True

    
        m = len(strs)
        if m == 1:
            return [[strs[0]]]

        resultant = []
        visited = [False] * m  # to avoid duplicates

        for i in range(m):
            if not visited[i]:
                ans = [strs[i]]
                visited[i] = True
                for j in range(i+1, m):
                    if not visited[j] and to_check_Anagram(strs[i], strs[j]):
                        ans.append(strs[j])
                        visited[j] = True
                resultant.append(ans)
        return resultant




            

