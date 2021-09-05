# PROBLEM: Find duplicate number
# https://leetcode.com/problems/find-the-duplicate-number/


from typing import List

# SOLUTION
def duplicate(nums: List[int]) -> int:
    for i in range(len(nums)):
        index = abs(nums[i]) - 1

        nums[index] *= -1

        if nums[index]>0:
            return abs(nums[i])

    return -1


if __name__ == "__main__":
    # INPUT :
    nums = [3,1,3,4,2]

    # OUTPUT :
    print(duplicate(nums))