class Solution:


    # You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space,
    #  where m is the sum of lengths of all the strings and n is the number of strings.

    def encode(self, strs: List[str]) -> str:

        parts = []

        for word in strs:
            length = str(len(word))
            parts.append(length)
            encoded_element = "#"
            parts.append(encoded_element)
            parts.append(str(word))


        return "".join(parts)

        


    def decode(self, s: str) -> List[str]:


        i, res = 0 , []
        n = len(s)


        while (i < n):
            
            j = i
            while ((j < n) and (s[j] != "#")):
                j += 1
            
            length = int(s[i:j])


            start = j + 1

            word = s[start : start + length]

            res.append(word)

            i = start + length


        return res
        





        
        

        





