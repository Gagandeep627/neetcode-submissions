class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        if numCourses == 0:
            return []

        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses


        for (a,b) in prerequisites:
            graph[b].append(a)
            indegree[a] += 1


        q = deque()


        for i in range(numCourses):
            if (indegree[i] == 0):
                q.append(i)

        result = []

        while (q):
            course = q.popleft()
            result.append(course)

            for neigh in graph[course]:
                indegree[neigh] -= 1

                if (indegree[neigh] == 0):
                    q.append(neigh)


        
        if (len(result) == numCourses):
            return result
        else:
            return []

                




            
    

