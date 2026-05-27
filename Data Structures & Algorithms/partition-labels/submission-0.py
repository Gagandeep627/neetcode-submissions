class Solution:
    def partitionLabels(self, s: str) -> List[int]:



        # topic : 2-pointers // Greeedy's solutions:-

        last = {}


        for i , ch in enumerate(s):
            last[ch] = i


        start = 0
        end = 0
        res = []


        for i , ch in enumerate(s):
            end = max(end, last[ch])

            if (i == end):
                size = (end-start+1)
                res.append(size)
                start=end+1

        
        return res

        