class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

            # Topic : Sliding Window Concept.. : .. ??

            #assigning freq dictionary && left && max_len variables.. ++ : ++ ??
            left = 0
            max_len = 0
            max_freq = 0
            freq = {}
            n =len(s)

            #Scans each element for once for left and right element : O(n)
            for right in range(n):
                #case 1: assign each element to its frequeny in the freq dictionary...
                freq[s[right]] = freq.get(s[right], 0) + 1
                max_freq = max(max_freq, freq[s[right]])
                
                #case 2: (length of our sub_string - max_frequency of the character to be replaced)
                #if it will be greater then the value of the K th most freqn to be usredc as per question..
                while ((right - left + 1) - max_freq) > k:
                    #shrink the substring via changing the freq of s[left] -= 1
                    freq[s[left]] -= 1
                    #Move left to += 1
                    left += 1


                #change max_len = to maximum length of substring which is : (right - left + 1)
                max_len = max(max_len , (right - left + 1))


            #Time_Complexity : O(n)
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



        