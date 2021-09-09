# PROBLEM: First missing positive
# https://leetcode.com/problems/first-missing-positive/
# https://www.interviewbit.com/problems/first-missing-integer/


from typing import List


# SOLUTION
def missing_positive (nums: List[int]) -> int:
    n = len(nums)

    for i in range(n):
        while nums[i]>0 and nums[i]<=n and nums[nums[i]-1] != nums[i]:
            nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
    
    for i in range(n):
        if nums[i] != i+1:
            return i+1

    return n+1


if __name__ == "__main__":
    # INPUT :
    nums = [7,8,9,11,12,-3]

    # OUTPUT :
    print(missing_positive(nums))
