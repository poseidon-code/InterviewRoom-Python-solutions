# PROBLEM: Find kth smallest element in matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List
import heapq

# SOLUTION
def k_smallest (matrix: List[List[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    result = -1

    pq = []
    for r in range (min(k, m)):
        heapq.heappush(pq, (matrix[r][0], r, 0))

    for i in range(k):
        result, r, c = heapq.heappop(pq)
        if c+1<n: heapq.heappush(pq, (matrix[r][c+1], r, c+1))
    
    return result


if __name__ == "__main__":
    # INPUT :
    matrix = [[1,5,9], [10,11,13], [12,13,15]]
    k = 8

    # OUTPUT :
    print(k_smallest(matrix, k))