class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:




            # topic : brute force solutions:-

            temp = []

            for num in arr:
                res = abs(x - num)
                temp.append((res, num))


            temp.sort()
            

            ans = []

            for i in range(k):

                ans.append(temp[i][1])

            ans.sort()

            return ans
            
