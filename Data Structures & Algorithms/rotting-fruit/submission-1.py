class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        


        # topic : BFS (matrix BFS solutions)...


        
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()


        # 1)check for all rotten fruits in the
        # matrix add their (row, column, minutes = (initial : 0))
        # in the queue -->
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    # if fresh fruit encountered -->
                    # maintain the count of (fresh) --> fruit for
                    # the matrix..
                    fresh += 1

        if (fresh == 0): #any of fresh fruit doesnt exists --> return : 0;
            return 0
        minutes = 0 #set minutes initially to 0;
        directions = [(1,0), (-1,0), (0,1), (0,-1)] #set directions up, down, right, left


        # check for queue untill any fresh fruit exited in the queue so far...
        while (q):
            # for every (row, colns, minute) -->
            x,y, minute = q.popleft()

            minutes = minute
            
            # for each possible directions so far..
            for (dx, dy) in directions:
                # calculated 1 step possible directions (nx, ny) -->
                nx, ny = x + dx, y + dy


                # check for out of bpunds of the nx, ny and check for fresh fruit if existed at
                # that point-->
                if ((0<=nx<rows) and (0<=ny<cols) and (grid[nx][ny] == 1)):
                    # set it to the rotten fruits-->
                    grid[nx][ny] = 2
                    # minimize fresh fruit;
                    fresh -= 1
                    # add(nx, ny, minutes + 1) --> to the queue-->
                    q.append((nx,ny, minute+1))



#         We visit every cell at most once → O(m × n) time

# Queue stores at most all cells → O(m × n) space

        return minutes if fresh <= 0 else -1       
                
