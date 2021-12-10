# PROBLEM: Minimum jump to reach end
# https://leetcode.com/problems/jump-game-ii/
# https://www.interviewbit.com/problems/min-jumps-array/

from typing import List

# SOLUTION
def jump (nums: List[int]) -> int:
    jumps = 0
    ce, cf = 0, 0

    for i in range(len(nums)-1):
        cf = max(cf, i+nums[i])

        if i == ce:
            jumps+=1
            ce = cf
        
    return jumps


if __name__ == "__main__":
    # INPUT :
    nums = [2,3,1,1,4]

    # OUTPUT :
    print(jump(nums))