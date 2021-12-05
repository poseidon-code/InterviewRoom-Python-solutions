# PROBLEM: House Robber
# https://leetcode.com/problems/house-robber/

from typing import List

# SOLUTION
def rob (nums: List[int]) -> int:
    a, b, n = 0, 0, len(nums)
    
    for i in range(n):
        if i%2==0:
            a = max(a+nums[i], b)
        else:
            b = max(a, b+nums[i])
    
    return max(a, b)


if __name__ == "__main__":
    # INPUT :
    nums = [1,2,3,1]

    # OUTPUT :
    print(rob(nums))