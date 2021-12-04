# PROBLEM: Maximum subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List

# SOLUTION
def max_subarray (nums: List[int]) -> int:
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    result = dp[0]

    for i in range(1,n):
        dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
        result = max(result, dp[i])

    return result


if __name__ == "__main__":
    # INPUT :
    nums = [5,4,-1,7,8]

    # OUTPUT :
    print(max_subarray(nums))