class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9
        # set for rows 9 sets in the array. = rows
        rows = [set() for _ in range(n)]
        # set for rows 9 sets in the array. = solns
        colns = [set() for _ in range(n)]
        # set for rows 9 sets in the array. = boxes
        boxes = [set() for _ in range(n)]



        # loop i till n
        for i in range(n):
            # loop j till n
            for j in range(n):
                # take num equals to board[i][j]
                num = board[i][j]


                # if num is commuting to . then  just continue
                # with the loop
                if num == ".":
                    continue

                # now evaluate 
                # box_index = (i // 3) (remainder on divisioin via 3) * 3
                # (j // 3) remainder on divisioin via 3)
                # || above is formula to evaluate the box_index
                # for a box of 9 * 9 
                # to reach to its exact cell for comutations
                box_index = (i // 3) * 3 + (j // 3)

                # if num is in same rows rows[i]
                # or num is in same columns checked via colns[j]
                # or num is in the same box boxes[box_index]
                # then our result will commute to False
                # answer : False
                # return False
                if ((num in rows[i]) or (num in colns[j]) or (num in boxes[box_index])):
                    return False
                
                # add that visited num n particular (i,j) position
                #  in the particular row of index : i -> via .adding(the num)
                # in the poarticular column of index : j -> via .adding(the num)
                # boxes[index : box_index] adding (that particular : num)
                rows[i].add(num)
                colns[j].add(num)
                boxes[box_index].add(num)


        # else all error cases failed only in that case...
        # after checking for all the cases may containg the error will
        # // would have thrown false the same num is been present 
        # in the same row , column , and within the same box of (9 * 9) boxes
        # else: its a valid box after checkig with the all validations
        # for the nums in the row , column and boxes
        # answer : True
        # return True;
        return True







    #    method 1 : most optimal approach -- O(n ^ 2) time complexity -- O(n ^ 2) space
    # complexity...

        n = 9
        rows = [set() for _ in range(n)]
        colns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)
                if ((num in rows[i]) or (num in colns[j]) or (num in boxes[box_index])):
                    return False
                rows[i].add(num)
                colns[j].add(num)
                boxes[box_index].add(num)


        # else all error cases failed only in that case...
        return True











        