class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        




        # topic : brute force solutions-->
        hand.sort()

        

        n = len(hand)

        if (n % groupSize != 0):
            return False

        used = [False] * n



        for i in range(n):

            if used[i]:
                continue

            start = hand[i]

            need = start

            found = False

            for size in range(groupSize):
                found = False
                for j in range(i,n):

                    if (not used[j] and hand[j] == need):
                        used[j] = True
                        found = True
                        need += 1
                        break

                # need += 1

                if (not found):
                    return False

                # found = False


        return True

                

            