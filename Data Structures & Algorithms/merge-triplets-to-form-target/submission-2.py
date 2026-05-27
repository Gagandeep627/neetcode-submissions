class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        

        # topic : Brute-Force solutions required so far... : ??
        # topic : Optimal_solutions so far for this questions.. : ??

        # time : O(n), space : O(1)
        x,y,z = target

        have_x, have_y, have_z = 0,0,0



        for (a,b,c) in triplets:
            
            if (a<=x and b<=y and c<= z):
                if (a >= have_x):
                    have_x = a
                if (b >= have_y):
                   have_y = b
                if (c >= have_z):
                    have_z = c



        return [have_x, have_y, have_z] == [x,y,z] 









            




