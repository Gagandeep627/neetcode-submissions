class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        



        # topic : BFS : (kahn's algorithm) -->

#         🌟 WHY BFS (Kahn’s Algorithm) SOLVES IT?

# Think of courses like tasks you need to complete.

# Some tasks have no dependency — they don’t require anything before them.
# These tasks can be done immediately.

# ✔ Step 1 — Start With Tasks That Need Nothing

# Courses with 0 prerequisites are "free."
# You can take them right away.

# So we put all these courses in a queue.

# Example:
# If Course 3 and Course 5 need nothing → put them in the queue first.

# ✔ Step 2 — Finish Those Tasks

# Take a course from the queue → mark it as completed.

# ✔ Step 3 — Completing a Course Frees Other Courses

# Imagine you have this dependency:

# 0 → 1


# Meaning:
# Course 1 needs Course 0 first.

# When you complete 0, course 1 now needs one less prerequisite.

# If course 1 ends up needing 0 prerequisites, it becomes "free" and is added to the queue.

# ✔ Step 4 — Keep Repeating

# You:

# Take free courses

# Reduce dependencies of other courses

# Add newly free courses to the queue

# This continues until no more courses can be freed.

# ❗ The Big Check

# If you were able to complete all courses this way →

# 👉 There was NO CYCLE
# 👉 It is possible to finish all courses

# But if some courses never become free, meaning their prerequisites never reduce to zero →

# 👉 Those courses are part of a CYCLE
# 👉 You will never be able to take them
# 👉 So finishing all courses is impossible

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

        





        

    