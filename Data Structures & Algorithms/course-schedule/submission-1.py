class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        



        # topic : BFS : (kahn's algorithm) -->

        graph = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses


        for (a,b) in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(len(indegree)):
            if (indegree[i] == 0):
                q.append(i) 

        taken_course = 0

        while (q):
            course = q.popleft()
            taken_course += 1


            for neigh in graph[course]:
                
                indegree[neigh] -= 1


                if (indegree[neigh] == 0):
                    q.append(neigh)

        # Time = O(V + E),
        # Space = O(V + E)|
        return taken_course == numCourses

        





        

    