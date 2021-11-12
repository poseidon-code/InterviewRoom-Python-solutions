# PROBLEM: Find kth largest element in a stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq

# SOLUTION
pq = []
qsize = 0

def k_largest(k: int, nums: List[int]):
    global pq, qsize
    pq = nums
    qsize = k
    heapq.heapify(pq)
    while len(pq) > k:
        heapq.heappop(pq)
    
def add(val: int) -> int:
    global pq, qsize
    if len(pq) < qsize:
        heapq.heappush(pq, val)
    elif val > pq[0]:
        heapq.heapreplace(pq, val)
    return pq[0]


if __name__ == "__main__":
    # INPUT :
    k = 3
    nums = [4,5,8,2]
    inputs = [3,5,10,9,4]

    # OUTPUT :
    k_largest(k, nums)
    for i in inputs:
        print(add(i))
