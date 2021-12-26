# PROBLEM: Cycle in a directed graph
# https://leetcode.com/problems/course-schedule/
# https://www.interviewbit.com/problems/cycle-in-directed-graph/

from typing import List

# SOLUTION
def can_finish (courses: int, prerequisites: List[List[int]]) -> bool:
    G = [[] for _ in range(courses)]
    degree = [0] * courses
    
    for j, i in prerequisites:
        G[i].append(j)
        degree[j] += 1
    
    bfs = [i for i in range(courses) if degree[i]==0]
    
    for i in bfs:
        for j in G[i]:
            degree[j] -= 1
            if degree[j] == 0:
                bfs.append(j)
    
    return len(bfs) == courses


if __name__ == "__main__":
    # INPUT :
    courses = 2
    prerequisites = [[1,0],[0,1]]

    # OUTPUT :
    print(can_finish(courses, prerequisites))