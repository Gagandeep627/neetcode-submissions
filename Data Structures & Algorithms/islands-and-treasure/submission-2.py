from collections import deque
INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

         # topic : BFS (Brute force solutions -- ((level-order search)))-->

        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0):
                    q.append((i, j))


        
        while (q):

            x,y = q.popleft()


            for (dx, dy) in directions:
                nx, ny = x + dx, y + dy
            

                if (0<= nx <m and 0<= ny<n and grid[nx][ny] == INF):
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx,ny))



    





























        

        # topic : BFS (Brute force solutions -- ((level-order search)))-->
        # 
        # m, n = len(grid), len(grid[0])
        
        # directions = [(1,0), (-1, 0), (0,1), (0,-1)]
     
        # def bfs_from_cell(r,c):
            
        #     visited = [[False] * n for _ in range(m)]
        #     queue = deque()
        #     queue.append((r,c,0))
            
        #     visited[r][c] = True

        #     while queue:

        #         x,y,dist = queue.popleft()

        #         if grid[x][y] == 0:
        #             return dist

        #         for (dx, dy) in directions:
        #             nx = x + dx
        #             ny = y + dy

        #             if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != -1:
        #                 visited[nx][ny] = True
        #                 queue.append((nx, ny, dist+1))

        #     return INF 


        # for r in range(m):
        #     for c in range(n):
        #         if (grid[r][c] == INF):
        #             dist = bfs_from_cell(r,c)
        #             grid[r][c] = dist

        # ⏱ Time Complexity : ⭐ O((m × n) × (m × n)) = O((mn)²)
#         | Type      | Complexity   |
# | --------- | ------------ |
# | **Time**  | **O((mn)²)** |
# | **Space** | **O(mn)**    |

        # return grid

        
