# PROBLEM: Alien Dictionary
# https://practice.geeksforgeeks.org/problems/alien-dictionary/1/?category[]=Graph&category[]=Graph&page=1&query=category[]Graphpage1category[]Graph

from typing import List

# SOLUTION
def order (d: List[str], n: int, k: int) -> str:
    adjs = {chr(ord('a') + i): [] for i in range(k)}

    for i in range(k):
        for s1, s2 in zip(d[:len(d)-1], d[1:]):
            if len(s1) - 1 < i or len(s2) - 1 < i:
                continue
            if s1[:i] == s2[:i] and (s1[i] != s2[i]) and (s1[i] not in adjs[s2[i]]):
                adjs[s2[i]].append(s1[i])

    visited = [False] * k
    p_order = []

    def _dfs(i):
        visited[i] = True
        c = chr(ord('a') + i)
        for w in adjs[c]:
            j = ord(w) - ord('a')
            if not visited[j]:
                _dfs(j)
        p_order.append(c)

    for i in range(k):
        if not visited[i]:
            _dfs(i)

    return ''.join(p_order)



if __name__ == "__main__":
    # INPUT :
    d = ["caa", "aaa", "aab"]
    n = 3
    k = 3

    # OUTPUT :
    print(order(d, n, k))