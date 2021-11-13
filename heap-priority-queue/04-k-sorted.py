# PROBLEM: Sort a nearly sorted array
# https://www.geeksforgeeks.org/nearly-sorted-algorithm/

from typing import List
import heapq

# SOLUTION
def k_sorted (nums: List[int], k: int) -> List[int]:
    size = k if len(nums)==k else k+1
    pq = nums[:size]
    heapq.heapify(pq)

    index = 0
    for i in range(size, len(nums)):
        nums[index] = heapq.heappop(pq)
        heapq.heappush(pq, nums[i])
        index += 1

    while pq:
        nums[index] = heapq.heappop(pq)
        index +=1

    return nums


if __name__ == "__main__":
    # INPUT :
    nums = [2,6,3,12,56,8]
    k = 3

    # OUTPUT :
    result = k_sorted(nums, k)
    print(result)
