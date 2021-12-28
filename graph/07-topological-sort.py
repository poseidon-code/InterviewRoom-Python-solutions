# PROBLEM: Topological Sort (Course Schedule 2)
# https://leetcode.com/problems/course-schedule-ii/

from typing import List

# SOLUTION
def find_order (courses: int, prerequisites: List[List[int]]) -> List[int]:
    G = [[] for _ in range(courses)]
    indegree = [0] * courses
    ans = []
    
    for j, i in prerequisites:
        G[i].append(j)
        indegree[j] += 1
    
    q = []
    for i in range(courses):
        if indegree[i]==0 : q.append(i)
    
    while len(q)!=0:
        cur = q.pop(0)
        ans.append(cur)

        for nextCourse in G[cur]:
            indegree[nextCourse] -= 1
            if indegree[nextCourse] == 0:
                q.append(nextCourse)
    
    if len(ans) == courses : return ans
    return []


if __name__ == "__main__":
    # INPUT :
    courses = 2
    prerequisites = [[1,0]]

    # OUTPUT :
    print(find_order(courses, prerequisites))