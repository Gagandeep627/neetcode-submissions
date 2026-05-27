class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        if not digits:
            return []


        res = []
        # path = []
        # topic : backtracking...

        phone_mappings = {"2" : "abc", "3": "def", "4" : "ghi", "5":"jkl",
         "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "0" :"+"}



        def back(idx, path):
            # base case 1 : when idx == len(digits) then
            # join the path as a string to the --> res;
            if (idx == len(digits)):
                res.append("".join(path))
                return

            # find out which is curr digit (mapped letter) at that idx
            curr_digit = digits[idx]

            # then loop through the eac and every element for the
            #  phone_mappings[curr_digit]:
            for ch in phone_mappings[curr_digit]:
                # add ch to the path-->
                path.append(ch)
                # back(idx + 1, path : ["d"])--> go deeper-->
                back(idx + 1, path)

                # then backtrack through the path
                #  --> and explore other possibilities--> 
                path.pop()


        # bacltrack (idx : 0, path : [])
        back(0, [])

        # Time
# Explore 4 choices per digit × build words O(n × 4ⁿ)
        return res





            







        



        # back()