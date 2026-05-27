class Solution:
    def partitionLabels(self, s: str) -> List[int]:



        # topic : 2-pointers // Greeedy's solutions:-

        last = {} #Maximum possible keys = 26 : O(26)

        # → runs n times → O(n)
        # step 1 : loop through the string with index
        
        for i , ch in enumerate(s):
            # Each loop does only constant-time operations.
            # for each chars overwrite its index, 
            # this ensures we finally store the last occurence:-
            last[ch] = i


        start = 0
        end = 0
        res = []

        # → runs n times → O(n) (greedy partitioning)
        # step 2 : traverse string to form partitions (greedy):
        for i , ch in enumerate(s):
            # Each loop does only constant-time operations.
            # update the partition end ot the farthest last occurence
            # of the chars seen so far
            end = max(end, last[ch])
            # if current index reaches partitions end,
            # it means all chars in this partition
            # do not appear in the string
            if (i == end):
                # size of partition= end - start + 1
                size = (end-start+1)
                res.append(size)
                # move start to the next index for new partitions
                start=end+1

            # 🔥 Total Time Complexity : O(n)+O(n)=O(n)
            # 🔥 Space Complexity : O(26)=O(1)
        # return the list of partition sizes:
        return res

        