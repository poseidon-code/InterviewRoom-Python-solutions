# PROBLEM: Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

# SOLUTION
def mps (nums: List[int]) -> int:
    n, l, r = len(nums), 0, 0
    result = nums[0]

    for i in range(n):
        l = (l if l else 1) * nums[i]
        r = (r if r else 1) * nums[n-1-i]
        result = max(result, max(l, r))

    return result



if __name__ == "__main__":
    # INPUT :
    nums = [2,3,-2,4]

    # OUTPUT :
    print(mps(nums))