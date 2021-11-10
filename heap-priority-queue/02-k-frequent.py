# PROBLEM: Find top k frequent elements
# https://leetcode.com/problems/top-k-frequent-elements/


import collections
from typing import List


# SOLUTION
def k_frequent (nums: List[int], k: int) -> List[int]:
    counts = collections.defaultdict(int)
    for i in nums : counts[i]+=1

    buckets = [[] for _ in range(len(nums)+1)]
    for i, count in counts.items():
        buckets[count].append(i)
    
    result = []
    for i in range(len(buckets)-1, -1, -1):
        if buckets[i]:
            for n in buckets[i]:
                result.append(n)
    
    return result[:k]


if __name__ == "__main__":
    # INPUT :
    nums = [1,1,1,2,2,3]
    k = 2

    # OUTPUT :
    print(k_frequent(nums, k))