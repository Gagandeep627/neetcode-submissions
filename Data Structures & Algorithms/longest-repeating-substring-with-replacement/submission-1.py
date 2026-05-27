class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

            # Topic : Sliding Window Concept.. : .. ??


            left = 0
            max_len = 0
            max_freq = 0
            freq = {}
            n =len(s)

            for right in range(n):

                freq[s[right]] = freq.get(s[right], 0) + 1
                max_freq = max(max_freq, freq[s[right]])
                

                while ((right - left + 1) - max_freq) > k:
                    freq[s[left]] -= 1
                    left += 1


                max_len = max(max_len , (right - left + 1))



            return max_len























        # Topic : Brute Force Solution.. ++ : ++ ??
        # n = len(s)
        # max_len = 0
        # # O(n)
        # for i in range(n):
        #     # O(n)
        #     for j in range(i+1, n + 1):
        #         sub_string = s[i : j]

        #         freq = {}

        #         # O(n) worst case for n == len(sub_string)
        #         for ch in sub_string:
        #             freq[ch] = freq.get(ch, 0) + 1


        #         max_freq = max(freq.values())

        #         replacement_needed = len(sub_string) - max_freq


        #         if (replacement_needed <= k):
        #             max_len = max(max_len, len(sub_string))


        # #Time_Complexity : O(n * n * n) : O(n ^ 3)
        # return max_len



        