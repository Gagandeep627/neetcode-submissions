class Solution:
    def characterReplacement(self, s: str, k: int) -> int:



        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i+1, n + 1):
                sub_string = s[i : j]

                freq = {}


                for ch in sub_string:
                    freq[ch] = freq.get(ch, 0) + 1


                max_freq = max(freq.values())

                replacement_needed = len(sub_string) - max_freq


                if (replacement_needed <= k):
                    max_len = max(max_len, len(sub_string))


        
        return max_len



        