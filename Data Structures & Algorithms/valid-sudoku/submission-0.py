class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:




        # jehra logic sikhya he uhh better he ki -- submit marr
        # apne fher logic de regarding jinne vii doubt he uhh gpt
        # recondideration chh rakh te better he kii -- Move to nxt wrk , hune tu fhilhaul tu. ++ : ++ ??

        n = 9
        rows = [set() for _ in range(n)]
        colns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]




        for i in range(n):
            for j in range(n):
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











        