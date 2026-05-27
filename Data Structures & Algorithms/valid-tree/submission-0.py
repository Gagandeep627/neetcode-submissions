from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        if (len(edges) != (n-1)):
            return False

        graph = defaultdict(list)
        visited = []

        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        q.append(0)


        while q:
            node = q.popleft()

            visited.append(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    q.append(neigh)


        return len(visited) == n





        