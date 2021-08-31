# PROBLEM: 2 sum
# https://leetcode.com/problems/two-sum/
# https://www.interviewbit.com/problems/2-sum/
# https://practice.geeksforgeeks.org/problems/key-pair/0


from typing import List

# SOLUTION
def two_sum (nums: List[int], target: int) -> List[int]:
    map = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in map:
            return [map[m], i]
        else:
            map[n] = i


if __name__ == "__main__":
    # INPUT :
    nums = [2,7,11,15]
    target = 9

    # OUTPUT
    twosum = two_sum(nums, target)
    print(twosum)