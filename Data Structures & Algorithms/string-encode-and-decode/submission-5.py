class Solution:


    # You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space,
    #  where m is the sum of lengths of all the strings and n is the number of strings.

    def encode(self, strs: List[str]) -> str:    
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return "".join(parts)



    def decode(self, s: str) -> List[str]:

        # If empty (shouldn't happen with our encode), return []
        res = []
        i = 0
        n = len(s)
        while i < n:
            # find the separator '#'
            j = i
            # move j until we hit '#'
            while j < n and s[j] != '#':
                j += 1
            # j now at '#', substring s[i:j] is the length
            length = int(s[i:j])
            # the string starts at j+1 and has 'length' characters
            start = j + 1
            word = s[start:start + length]
            res.append(word)
            # move i to the next encoded item
            i = start + length
        return res

        





