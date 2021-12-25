# PROBLEM: Cycle in undirected graph
# https://www.interviewbit.com/problems/cycle-in-undirected-graph/
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1/?category{]=Graph&category[]=Graph&page=1&query=category[]Graphpage1category[]Graph


from typing import List

# SOLUTION
def dfs (adj: List[List[int]], v: List[bool], p: int, s: int) -> bool:
    v[s] = True

    for i in adj[s]:
        if v[i]==False:
            if dfs(adj, v, s, i):
                return True
        elif i!=p:
            return True
    
    return False


def is_cycle (graph: List[List[int]], n: int) -> bool:
    v = [False]*(n+1)
    adj = [[]]*(n+1)
    adj[0].append(-1)

    for i in range(len(graph)):
        adj[graph[i][0]].append(graph[i][1])
        adj[graph[i][1]].append(graph[i][0])

    for i in range(1, n+1):
        if v[i]==False:
            if dfs(adj, v, -1, i):
                return True
    
    return False


if __name__ == "__main__":
    # INPUT :
    n = 5
    graph = [[1,2],[1,3],[2,3],[1,4],[4,5]]

    # OUTPUT :
    print(is_cycle(graph, n))