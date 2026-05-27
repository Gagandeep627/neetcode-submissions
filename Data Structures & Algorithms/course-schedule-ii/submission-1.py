class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        


        # topic : BFS (topological sort - Kahn's algo)-->

        if numCourses == 0:
            return []

        # step 1 : build a graph for each index (i) --> 
        # step 2 : indegree array

        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        

        # 3).for all dpendencies for (a, b) in the prequistuises
        # add it to the graph[b].append(a) -->
        # ++ indegree[a] += 1

        for (a,b) in prerequisites:
            graph[b].append(a)
            indegree[a] += 1


        q = deque()

        # 4).create a deqeue --> all indexes corrosponding to 0
        # should be added to the queue (q)-->

        for i in range(numCourses):
            if (indegree[i] == 0):
                q.append(i)

        result = []

        # 5).create a resultant-->
        # remove element from the front of the q-->
        # add(course) --> result
        # for neigh in graph[course]: deduce (indegree[neigh] -= 1)
        # if (indegree[neigh] == 0): add it to q add(neigh) -->

        while (q):
            course = q.popleft()
            result.append(course)

            for neigh in graph[course]:
                indegree[neigh] -= 1

                if (indegree[neigh] == 0):
                    q.append(neigh)

        #6). no. corrosponding to the len(result):-->return result;
        # else return empty [];
        
        if (len(result) == numCourses):
            return result
        else:
            return []

        # ⏱ Time Complexity — O(V + E)|
        # 💾 Space Complexity — O(V + E)|

                




            
    

